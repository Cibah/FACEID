import datetime
import os
from src.config.Configurator import Configurator
from src.danalock.Danalock import openDoor, lockDoor
from src.doorbird.Doorbird import waitForEventAndDownloadImage
from src.incidents.Mail import sendMail
from src.log.Logger import logger
from src.machine_learning.Cropper import crop
from src.machine_learning.FaceML import FaceML
from src.machine_learning.barcode_scanner import findQR

version = "0.0.1"


def main():
    # Login for Events
    logger.debug("FaceID by HFU v")
    failed_access = 0
    # init
    ml = FaceML()

    while True:
        image = waitForEventAndDownloadImage()

        qrtuple = findQR(image)
        logger.debug(qrtuple[1])
        if qrtuple[0]:
            if qrtuple[1] == "mew63xy93kfhe":
                sendMail("Add Known Face", [image])
                # Danalock.open()
                currentdate = datetime.datetime.now().timestamp()
                filePath1 = Configurator.get("data", "data_path_known_faces")
                filePath = filePath1 + currentdate + '.jpg'
                crop(image, filePath )
                ml.load_known_faces()
            elif qrtuple[1] =="check out":
                result = ml.check_face(image)
                if result[0]:
                    # find face in known faces and delete it
                    os.remove(result[1])
                    ml.load_known_faces()
                    sendMail("Remove known face!", result[1])
                else:
                    sendMail("Wanted to remove a known face, but could not find the regarding face!", image)
        else:
            person_known = ml.check_face(image)
            if person_known:
                # open door
                logger.debug("Open the door for authorised person...")
                openDoor()
            else:
                # do not open door
                logger.debug("No access!")
                failed_access += 1
                if failed_access > int(Configurator.get("general", "max_num_of_failed_access")):
                    sendMail("5 failed attempts to access", image)
                    lockDoor()


if __name__ == '__main__':
    main()

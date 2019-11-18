import datetime
import os

from src.config import Configurator
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
    ml = FaceML(Configurator.get("data", "data_path_known_faces"))

    while True:
        image = waitForEventAndDownloadImage()

        qrtuple = findQR()
        if qrtuple[0]:
            if qrtuple[1] == "register":
                sendMail("Add Known Face", image)
                # Danalock.open()
                currentdate = datetime.datetime.now().timestamp()
                crop(image, Configurator.get("data", "data_path_known_faces") + currentdate)
                ml.load_known_faces()
            elif qrtuple[1] == "deregister":
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
            if person_known[0]:
                # open door
                logger.debug("Open the door for " + person_known[1])
                openDoor()
            else:
                # do not open door
                logger.debug("No access!")
                failed_access += 1
                if (failed_access > Configurator.get("general", "max_num_of_failed_access")):
                    sendMail("5 failed attempts to access", image)
                    lockDoor()


if __name__ == '__main__':
    main()

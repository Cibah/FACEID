import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
import os
from src.machine_learning.Cropper import crop
from src.machine_learning.FaceML import FaceML
from src.config.Configurator import Configurator
from src.danalock.Danalock import openDoor, lockDoor
from src.doorbird.Doorbird import waitForEventAndDownloadImage
from src.incidents.Mail import sendMail
from src.log.Logger import logger
from src.machine_learning.barcode_scanner import findQR

version = "0.0.1"


def main():
    # Login for Events
    logger.debug("FaceID by HFU v")
    failed_access = 0
    # init
    ml = FaceML()

    qr_register = Configurator.get("machine_learning", "qr_register_key")
    qr_unregister = Configurator.get("machine_learning", "qr_unregister_key")

    #TODO: Check Keep-alive of doorbird
    while True:
        image = waitForEventAndDownloadImage()
        qrtuple = findQR(image)
        if image == "ERROR":
            logger.error("No Image was downloaded from the Doorbird")
            continue

        if qrtuple[0]:
            if qrtuple[1] == qr_register:
                # Danalock.open()
                logger.info('Register face')
                currentdate = datetime.datetime.now().timestamp()
                file_path_partial = Configurator.get("data", "data_path_known_faces")
                path = os.path.dirname(os.path.abspath(__file__))
                final = path + '/..' + file_path_partial
                file_path = final + str(currentdate) + '.jpg'
                logger.warn(file_path)
                if crop(image, file_path):
                    ml.load_new_face(file_path)
                    sendMail("Add Known Face", [image])
                    openDoor()
                else:
                    logger.error("No Face found in registering image " + image)
                # ml.load_known_faces()
            elif qrtuple[1] == qr_unregister:
                logger.warn(image)
                results = ml.check_face(image)
                for result in results:
                    if result:
                        # find face in known faces and delete it
                        sendMail("Remove known face!", [result])
                        os.remove(result)
                        ml.load_known_faces()
                    else:
                        sendMail("Wanted to remove a known face, but could not find the regarding face!", image)

        else:
            person_known = ml.check_face(image)
            if person_known:
                # open door
                logger.info("Open the door for authorised person...")
                openDoor()
            else:
                # do not open door
                logger.info("No access!")
                failed_access += 1
                if failed_access > int(Configurator.get("general", "max_num_of_failed_access")):
                    sendMail("5 failed attempts to access", image)
                    lockDoor()


if __name__ == '__main__':
    main()

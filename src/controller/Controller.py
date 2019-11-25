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
from PIL import Image

version = "0.0.1"


def main():
    # Login for Events
    logger.debug("FaceID by HFU v")
    failed_access = 0
    # init
    ml = FaceML()

    qr_register = Configurator.get("machine_learning", "qr_register_key")
    qr_unregister = Configurator.get("machine_learning", "qr_unregister_key")

    while True:
        raw_image = waitForEventAndDownloadImage()

        # Resize image to improve detection of QR-Codes
        size = 1920, 1080
        im = Image.open(raw_image)
        im_resized = im.resize(size, Image.ANTIALIAS)

        # convert jpg to png to improve QR-Code detection
        raw_im_jpg = raw_image.split('.')[0]
        image = raw_im_jpg + ".png"
        im_resized.save(image, "PNG")

        qrtuple = findQR(image)
        logger.debug(qrtuple[1])
        if qrtuple[0]:
            if qrtuple[1] == qr_register:
                sendMail("Add Known Face", [image])
                # Danalock.open()
                currentdate = datetime.datetime.now().timestamp()
                file_path_partial = Configurator.get("data", "data_path_known_faces")
                file_path = file_path_partial + str(currentdate) + '.jpg'
                crop(image, file_path )
                ml.load_known_faces()
            elif qrtuple[1] == qr_unregister:
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

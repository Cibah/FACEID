# import the necessary packages
# HOW TO USE THIS:  python3 barcode_Scanner.py --image ../../img/test1.png
# import os

import PIL
import cv2
import numpy
from PIL import Image
from pyzbar import pyzbar
from src.log.Logger import logger


def findQR(pathToImage):
    isQR = False
    qrkey = ""

    # First resize the image with PIL
    im = Image.open(pathToImage)
    (width, height) = (im.width * 2, im.height * 2)
    im_resized = im.resize((width, height), resample=PIL.Image.NEAREST)
    logger.debug("Checking QR Codes in " + pathToImage)

    # Convert the PIL Image to opencv Image
    image = cv2.cvtColor(numpy.array(im_resized), cv2.COLOR_RGB2BGR)

    # Switch to grayscale mode
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)
    logger.debug("Found barcodes: " + str(barcodes))
    # loop over the detected barcodes
    for barcode in barcodes:
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        isQR = True
        qrkey = barcodeData
        # print the barcode type and data to the terminal
    result = (isQR, qrkey)
    return result

# for face in os.listdir("../../img/QrCodes/"):
#    if face.endswith(".jpg") or face.endswith(".png"):
#        findQR("../../img/QrCodes/"+ face)

# import the necessary packages
# HOW TO USE THIS:  python3 barcode_Scanner.py --image ../../img/test1.png
# import os
import os

import PIL
import cv2
import imutils as imutils
import numpy
from PIL import Image
from pyzbar import pyzbar
from src.log.Logger import logger
from PIL import ImageEnhance


#upscaling the picture
def upscale(image, scale):
    height, width = image.shape[:2]
    return cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_LINEAR)

#greyscaling the picture
def greyscale(image, iThresh):
    # return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(image, iThresh, 255, cv2.THRESH_BINARY)[1]

def findQR(pathToImage):
    if (pathToImage == "ERROR"):
        logger.error("Image not found! " + pathToImage)
        return False
    isQR = False
    qrkey = ""
    logger.debug("Checking QR Codes in " + pathToImage)
    img_original = cv2.imread(pathToImage)

    image = upscale(img_original, 3.0)
    barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        image = greyscale(image, 65)
        barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        image = upscale(img_original, 2.0)
        barcodes = pyzbar.decode(image)

    if len(barcodes) == 0:
        image = greyscale(image, 55)
        barcodes = pyzbar.decode(image)

    # loop over the detected barcodes
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        logger.debug("QR-Code found: " + barcodeData)
        isQR = True
        qrkey = barcodeData
    if not (isQR):
        logger.info("No QR-Code found")
    result = (isQR, qrkey)
    return result


processed = 0
found = 0

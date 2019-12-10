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


def upscale(image, scale):
    height, width = image.shape[:2]
    return cv2.resize(image, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_LINEAR)


def greyscale(image, iThresh):
    # return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(image, iThresh, 255, cv2.THRESH_BINARY)[1]

def findQR(pathToImage):
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
        print("No Code")
    result = (isQR, qrkey)
    return result


# processed = 0
# found = 0
# # print(findQR("../../img/QrCodes/test5_crop.jpg"))
#
# 
# for face in os.listdir("../../img/QrCodes/"):
#     if face.endswith(".jpg") or face.endswith(".png"):
#         processed += 1
#         if ((findQR("../../img/QrCodes/" + face))[0] == True):
#             found += 1
# print(str(found) + "/" + str(processed))

# import the necessary packages
# HOW TO USE THIS:  python3 barcode_Scanner.py --image ../../img/test1.png
import argparse
import cv2
from pyzbar import pyzbar
from src.config.Configurator import Configurator

# construct the argument parser and parse the arguments


# show the output image
# cv2.imshow("Image", image)
cv2.waitKey(0)


def findQR(pathToImage):
    isQR = False
    qrkey = ""

    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--image", required=True, help="path to input image")
    # ap.add_argument(pathToImage)
    # args = vars(ap.parse_args())

    # load the input image
    image = cv2.imread(pathToImage)

    # find the barcodes in the image and decode each of the barcodes
    barcodes = pyzbar.decode(image)

    qrkey=""
    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        isQR = True

        qrkey= barcodeData

        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

    result = (isQR, qrkey)
    return result

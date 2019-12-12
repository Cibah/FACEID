# Check events from openhab
# Check Making of an image

import unittest
import os
from src.doorbird.Doorbird import *
from PIL import Image


class DoorbirdTest(unittest.TestCase):


    def test_ImageDownload(self):
        print(os.getcwd())
        fileEnding = ".jpg"

        try:
            image = downloadImage()
            self.assertTrue(fileEnding in image)
            Image.open(image)
        except TimeoutError:
            self.fail("There was a timeouterror")
        except IOError:
            self.fail("Failed to open image!")


if __name__ == '__main__':
    unittest.main()

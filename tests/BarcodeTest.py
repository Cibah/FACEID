import unittest
from src.config.Configurator import Configurator
from src.machine_learning.barcode_scanner import findQR

class BarcodeTest(unittest.TestCase):

    def test_qr_detection(self):
        try:
            image = "test_register.png"
            qr_tuple = findQR(image)
            qr_detected = qr_tuple[0]
            self.assertTrue(qr_detected)
        except:
            self.fail("An error occured, could not detect QR-Code!")

    def test_qr_register(self):
        try:
            image = "test_register.png"
            qr_tuple = findQR(image)
            qr_detected = qr_tuple[0]
            qr_text = qr_tuple[1]
            qr_register = Configurator.get("machine_learning", "qr_register_key")
            self.assertEqual(qr_text, qr_register)
        except:
            self.fail("Error occured for registration code!")

    def test_qr_unregister(self):
        try:
            image = "test_unregister.png"
            qr_tuple = findQR(image)
            qr_detected = qr_tuple[0]
            qr_text = qr_tuple[1]
            qr_unregister = Configurator.get("machine_learning", "qr_unregister_key")
            self.assertEqual(qr_text, qr_unregister)
        except:
            self.fail("Error occured for deregistration code!")



if __name__ == '__main__':
    unittest.main()

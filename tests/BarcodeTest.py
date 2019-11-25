import unittest
from src.machine_learning.barcode_scanner import findQR
from src.config.Configurator import Configurator

class BarcodeTest(unittest.TestCase):

    def test_qr_detection(self):
        image = "test_detection.png"
        qr_tuple = findQR(image)
        qr_detected = qr_tuple[0]
        self.assertTrue(qr_detected)


    def test_qr_register(self):
        image = "test_register.png"
        qr_tuple = findQR(image)
        qr_detected = qr_tuple[0]
        qr_text = qr_tuple[1]
        qr_register = Configurator.get("machine_learning", "qr_register_key")
        self.assertEqual(qr_text, qr_register)


    def test_qr_unregister(self):
        image = "test_unregister.png"
        qr_tuple = findQR(image)
        qr_detected = qr_tuple[0]
        qr_text = qr_tuple[1]
        qr_unregister = Configurator.get("machine_learning", "qr_unregister_key")
        self.assertEqual(qr_text, qr_unregister)



if __name__ == '__main__':
    unittest.main()

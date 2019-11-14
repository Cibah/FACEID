import unittest
from src.klinkel.Klingel import klingel


class DoorbirdTest(unittest.TestCase):

    def test_import(self):
        #import from config file
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_bind_socket(self):
        #socket test
        #test functions
       
    def test_readData(self):
        #read data from socket
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
   
    def test_decryptData(self):
        #decrypt/parse udp data
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_webLogin(self):
        #login to Doorbird Web API
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        
    def test_httpRequest(self):
        #Send http Request for Doorbird picture
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6"
        
    def test_httpResponse(self):
        #Read httpResponse from Doorbird API, depends on httpRequest
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        
    def test_saveImage(self):
        #save Image returned from httpResponse to storage
        #define assertions from unittest.Testcase
        #self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
 
    
if __name__ == '__main__':
    unittest.main()

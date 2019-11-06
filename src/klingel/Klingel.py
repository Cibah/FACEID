#from src.middleware.Middleware import *
from src.log.Logger import logger
import socket

def login_and_wait_for_event():
    #import credentials from config file
    # Login with credentials
    logger.debug("Login in with " + user + " " + password + " to " + url)
    # store session id for other functions?
    # while True: listen for notifications of the button and fire event
    # Send image as parameter: url + "/bha-api/image.cgi"

def udpHandler():
    #Import Settings from Config file
    UDP_IP_ADDRESS = "0.0.0.0"
    UDP_PORT_NO = 35344
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    while True:
        data = serverSock.recvfrom(1024)
        message= data[0].decode()
        print ("Message: ", message)
        
def main():
    #do some udp stuff
    print("Starting udp server...")
    udpHandler()

if __name__ == '__main__':
    main()

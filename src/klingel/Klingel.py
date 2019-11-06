#from src.middleware.Middleware import *
from src.log.Logger import logger
import socket
import urllib.request
import ConfigParser
import io

def import_config():
    #import all relevant information
    with open("conf.ini") as f:
        sample_config = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(sample_config))
    print(config.get('doorbird', 'UDP_PORT_ONE'))
    
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

def httpRequest():
    #doorBirdGetImageUrl from config
    urllib.request.urlopen(doorBirdGetImageUrl).read()
    


def main():
    #do some udp stuff
    print("Starting udp server...")
    udpHandler()

if __name__ == '__main__':
    main()

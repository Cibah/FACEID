import socket
import urllib.request
import datetime
from src.config.Configurator import Configurator
from src.log.Logger import logger

udp_address = ""
udp_port = 0
door_bird_url = ""


def import_config(section):
    # get config dictionary all relevant information
    config = Configurator.get_config(section)

    # set values
    global udp_address
    global udp_port
    global door_bird_url
    udp_address = config.get("udp_ip_address")
    udp_port = config.get("udp_port_two")
    door_bird_url = config.get("door_bird_url")


def udphandler():
    # bind socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((udp_address, int(udp_port)))
    logger.debug("UDP service started on address: {} and port: {}".format(udp_address,udp_port))
    while True:
        data = server_sock.recvfrom(1024)

        try:
            message = data[0].decode()
            logger.debug("Keep-alive msg: {}".format(message))
        except:
            httpRequest()
            logger.debug("Message:", " An event has occured !")


def httpRequest():
    # request picture from API and save it
    logger.debug("sending http request...")
    currentdate = datetime.datetime.now().timestamp()
    filename = '/home/maik/FaceID/FACEID/img/unknown/%s.jpg' % (currentdate)
    urllib.request.URLopener().retrieve(door_bird_url, filename)


def main():
    # do some udp stuff
    logger.debug("Starting udp server...")
    import_config("doorbird")
    udphandler()


if __name__ == '__main__':
    main()

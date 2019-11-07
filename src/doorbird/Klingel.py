import socket
import urllib.request
from src.config.Configurator import Configurator

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
    udp_port = config.get("udp_port_one")
    door_bird_url = config.get("door_bird_url")


# def login_and_wait_for_event():
# import credentials from config file
# Login with credentials
# logger.debug("Login in with " + user + " " + password + " to " + url)
# store session id for other functions?
# while True: listen for notifications of the button and fire event++
# Send image as parameter: url + "/bha-api/image.cgi"


def udphandler():
    # bind socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind((udp_address, int(udp_port)))
    while True:
        data = server_sock.recvfrom(1024)
        message = data[0].decode()
        print("Message: ", hex(message))


def httpRequest():
    # request picture from API
    urllib.request.urlopen(door_bird_url).read()


def main():
    # do some udp stuff
    print("Starting udp server...")
    import_config("doorbird")
    udphandler()


if __name__ == '__main__':
    main()

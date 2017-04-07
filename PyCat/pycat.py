import argparse
import netaddr


def command(socket, cmd):
    "Exec Command"
    pass


def portCheck(port):
    "Boolean: check if a port is valid"
    pass


def ipCheck(ip):
    "Boolean: check if an ip address is valid"
    try:
        netaddr.IPNetwork(ip)
        return True
    except netaddr.AddrFormatError:
        return False
    pass


def main(ip, port):
    pass


if __name__ == '__main__':
    "Using argparse to get ip, port from input"
    parser = argparse.ArgumentParser(description='PyCat')
    parser.add_argument('-t', '--ip', type=str, help='IP for scan')
    parser.add_argument('-p', '--port', type=int, help='Port for scan')

    pycat = parser.parse_args()

    main(pycat.ip, pycat.port)
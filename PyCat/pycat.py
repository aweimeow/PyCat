import ipaddress


def command(socket, cmd):
    "Exec Command"
    pass


def portCheck(port):
    "Boolean: check if a port is valid"
    pass


def ipCheck(ip):
    "Boolean: check if an ip address is valid"
    try:
        ipaddress.IPv4Network(unicode(ip))
        return True
    except ValueError:
        return False
    pass


if __name__ == '__main__':
    "Using argparse to get ip, port from input"
    pass

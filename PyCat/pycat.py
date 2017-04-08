import argparse
import netaddr


def command(socket, cmd):
    "Exec Command"
    pass


def portCheck(port):
    "Boolean: check if a port is valid"
    try:
        if 0 <= int(port) <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False


def ipCheck(ip):
    "Boolean: check if an ip address is valid"
    try:
        if ip.count("/") == 1:
            ip, netmask = ip.split('/')
            p = list(map(lambda x: int(x), ip.split(".")))
            q = list(map(lambda x: int(x), netmask.split(".")))
            for x in p:
                if not 0 <= x <= 255:
                    return False
            if len(q) == 4:
                try:
                    mask = netaddr.IPAddress(netmask)
                    if not (mask.is_netmask() or mask.is_hostmask()):
                        return False
                except netaddr.AddrFormatError:
                    return False
            elif len(q) == 1:
                if not 0 <= q[0] <= 32:
                    return False
        elif ip.count(".") == 3:
            p = list(map(lambda x: int(x), ip.split(".")))
            for x in p:
                if not 0 <= x <= 255:
                    return False
        else:
            return False
    except ValueError:
        return False
    return True


def main(ip, port):
    pass


if __name__ == '__main__':
    "Using argparse to get ip, port from input"
    parser = argparse.ArgumentParser(description='PyCat')
    parser.add_argument('-t', '--ip', type=str, help='IP for scan')
    parser.add_argument('-p', '--port', type=int, help='Port for scan')

    pycat = parser.parse_args()

    main(pycat.ip, pycat.port)

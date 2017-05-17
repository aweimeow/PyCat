import argparse
import netaddr
import sys
import json


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


def main(ip, port=None):
    if not ipCheck(ip):
        sys.stderr.write("ERROR: Invalid ip\n")
        return json.dumps({"success": False})

    ports = []
    if port is None:
        ports = ["0-1023"]
    elif port.count("-") == 1:
        p = port.split("-")
        if len(p) != 2 or not portCheck(p[0]) or not portCheck(p[1]):
            sys.stderr.write("ERROR: Invalid port\n")
            return json.dumps({"success": False})
    else:
        for x in port.split(","):
            if not portCheck(x):
                sys.stderr.write("ERROR: Invalid port\n")
                return json.dumps({"success": False})
            ports.append(x)

    return json.dumps({"success": True})


def _main():
    "Using argparse to get ip, port from input"
    parser = argparse.ArgumentParser(description='PyCat')
    parser.add_argument('-t', '--ip', type=str,
                        help='IP for scan', required=True)
    parser.add_argument('-p', '--port', type=str, help='Port for scan')

    pycat = parser.parse_args()

    main(pycat.ip, pycat.port)

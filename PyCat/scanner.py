import socket


class Scanner:
    def __init__(self):
        self.timeout = 1

    def scanip(self, ip):
        try:
            socket.gethostbyaddr(ip)
        except:
            return False
        return True

    def scanport(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        return sock.connect_ex((ip, port))

    def scanports(self, ip="127.0.0.1", ports="0-65535"):
        assert ports.count('-') == 1
        src_port, dst_port = map(lambda x: int(x), ports.split('-'))

        if not self.scanip(ip):
            self.report = {"success": False, "ports": {}}
            return

        self.report = {"success": True, "ports": {}}

        for port in range(src_port, dst_port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            if sock.connect_ex((ip, port)) == 0:
                self.report["ports"][port] = True
            else:
                self.report["ports"][port] = False

            sock.close()

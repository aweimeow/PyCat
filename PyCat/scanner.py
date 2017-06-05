import time
import socket
import telnetlib


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

    def scanservice(self, ip, port):
        tn = telnetlib.Telnet(host=ip, port=port)

        timeout = 0
        service_info = ""

        while timeout < 1 and not service_info:
            service_info = tn.read_eager()
            timeout += 0.1
            time.sleep(0.1)

        if service_info:
            tn.close()
            return service_info.decode('utf-8')

        # Or Try to Connect with http Header

        tn.write(b'GET / HTTP/1.0\n\n\n')
        while timeout < 2 and not service_info:
            service_info = tn.read_eager()
            timeout += 0.1
            time.sleep(0.1)

        tn.close()

        return service_info.decode('utf-8')

    def scanports(self, ip="127.0.0.1", ports="0-65535"):
        assert ports.count('-') == 1
        src_port, dst_port = map(lambda x: int(x), ports.split('-'))

        if not self.scanip(ip):
            self.report = {"success": False, "ports": {}, "services": {}}
            return

        self.report = {"success": True, "ports": {}, "services": {}}

        for port in range(src_port, dst_port+1):
            if self.scanport(ip, port) == 0:
                self.report["ports"][port] = True
                service_info = self.scanservice(ip, port)
                if service_info:
                    self.report["services"][port] = service_info
            else:
                self.report["ports"][port] = False

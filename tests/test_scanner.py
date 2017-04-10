import random
import socket
import pytest

from PyCat.scanner import Scanner


@pytest.fixture(scope="module")
def Ports():
    MaxPort = 50050
    MinPort = 50000
    PortNums = 25

    ports = random.sample(range(MinPort, MaxPort), PortNums)
    ports_instance = []

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", port))
        s.listen(2)
        ports_instance.append(s)

    yield (ports, ports_instance)

    for instance in ports_instance:
        instance.close()


@pytest.mark.usefixtures("Ports")
class TestScanner:
    " Test PyCat's Scanner Functionality "

    def test_scanip(self):
        scanner = Scanner()
        assert scanner.scanip("127.0.0.1")
        assert scanner.scanip("8.8.8.8")
        assert not scanner.scanip("256.256.256.256")

    def test_scanport(self, Ports):
        scanner = Scanner()
        ports = Ports[0]
        for port in random.sample(range(50000, 50050), 30):
            if port in ports:
                assert scanner.scanport("127.0.0.1", port) == 0

    def test_scan_success(self, Ports):
        ports = Ports[0]
        result = {"success": True, "ports": {}}

        for port in range(50000, 50050):
            if port in ports:
                result["ports"][port] = True
            else:
                result["ports"][port] = False

        scanner = Scanner()
        scanner.scanports("127.0.0.1", "50000-50050")

        assert scanner.report == result

    def test_scan_failure(self):
        result = {"success": False, "ports": {}}

        scanner = Scanner()
        scanner.scanports("256.256.256.256", "0-65535")

        assert scanner.report == result

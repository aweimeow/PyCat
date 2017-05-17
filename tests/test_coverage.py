from PyCat import pycat
from PyCat.scanner import Scanner


class TestCoverage:
    def test_pycat_c0(self):
        assert not pycat.ipCheck("128.400,.128/#$%")
        assert not pycat.ipCheck("140.113.1.256/24")
        assert not pycat.ipCheck("128.128.128.128/255.255.0.0")
        assert not pycat.ipCheck("128.128.128.128/255.255.256.0")
        assert not pycat.ipCheck("140.113.1.1/40")
        assert pycat.ipCheck("140.113.1.1/24")

        assert json.loads(pycat.main("0.0.0.0", "17768"))["success"]
        assert not json.loads(pycat.main("140.113.1.1", "88888"))["success"]
        assert json.loads(pycat.main("0.0.0.0"))["success"]
        assert not json.loads(pycat.main("0.0.0.0", "1--2"))["success"]
        assert not json.loads(pycat.main("0.0.0.0", "80000,80001"))["success"]

        assert Scanner.scanip("0.0.0.0")
        assert not Scanner.scanip("256.256.256.256")


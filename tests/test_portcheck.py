from PyCat import pycat


class TestBoundaryValue:
    def test_WeakNormal(self):
        assert pycat.portCheck(0)
        assert pycat.portCheck("0")

        assert pycat.portCheck(65535)
        assert pycat.portCheck("65535")

    def test_WeakRobust(self):
        assert not pycat.portCheck(-1)
        assert not pycat.portCheck("-1")

        assert not pycat.portCheck(65536)
        assert not pycat.portCheck("65536")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        "Same as weak robust test"
        pass

from PyCat import pycat

class TestBoundaryValue:
    def test_WeakNormal(self):
        assert pycat.ipCheck("1.128.128.128") == True
        assert pycat.ipCheck("223.128.128.128") == True

        assert pycat.ipCheck("128.1.128.128") == True
        assert pycat.ipCheck("128.254.128.128") == True
        
        assert pycat.ipCheck("128.128.1.128") == True
        assert pycat.ipCheck("128.128.254.128") == True
        
        assert pycat.ipCheck("128.128.128.1") == True
        assert pycat.ipCheck("128.128.128.254") == True

    def test_WeakRobust(self):
        assert pycat.ipCheck("0.128.128.128") == False
        assert pycat.ipCheck("224.128.128.128") == False

        assert pycat.ipCheck("128.0.128.128") == False
        assert pycat.ipCheck("128.255.128.128") == False

        assert pycat.ipCheck("128.128.0.128") == False
        assert pycat.ipCheck("128.128.255.128") == False

        assert pycat.ipCheck("128.128.128.0") == False
        assert pycat.ipCheck("128.128.128.255") == False

    def test_StrongNormal(self):
        assert pycat.ipCheck("1.1.128.128") == True
        assert pycat.ipCheck("1.254.128.128") == True
        assert pycat.ipCheck("223.1.128.128") == True
        assert pycat.ipCheck("223.254.128.128") == True

        assert pycat.ipCheck("1.128.1.128") == True
        assert pycat.ipCheck("1.128.254.128") == True
        assert pycat.ipCheck("223.128.1.128") == True
        assert pycat.ipCheck("223.128.254.128") == True

        assert pycat.ipCheck("1.128.128.1") == True
        assert pycat.ipCheck("1.128.128.254") == True
        assert pycat.ipCheck("223.128.128.1") == True
        assert pycat.ipCheck("223.128.128.254") == True

        assert pycat.ipCheck("128.1.1.128") == True
        assert pycat.ipCheck("128.1.254.128") == True
        assert pycat.ipCheck("128.254.1.128") == True
        assert pycat.ipCheck("128.254.254.128") == True

        assert pycat.ipCheck("128.1.128.1") == True
        assert pycat.ipCheck("128.1.128.254") == True
        assert pycat.ipCheck("128.254.128.1") == True
        assert pycat.ipCheck("128.254.128.254") == True

        assert pycat.ipCheck("128.128.1.1") == True
        assert pycat.ipCheck("128.128.1.254") == True
        assert pycat.ipCheck("128.128.254.1") == True
        assert pycat.ipCheck("128.128.254.254") == True

        assert pycat.ipCheck("1.1.1.128") == True
        assert pycat.ipCheck("223.1.1.128") == True
        assert pycat.ipCheck("1.254.1.128") == True
        assert pycat.ipCheck("1.1.254.128") == True
        assert pycat.ipCheck("223.254.1.128") == True
        assert pycat.ipCheck("223.1.254.128") == True
        assert pycat.ipCheck("1.254.254.128") == True
        assert pycat.ipCheck("223.254.254.128") == True

        assert pycat.ipCheck("1.1.128.1") == True
        assert pycat.ipCheck("223.1.128.1") == True
        assert pycat.ipCheck("1.254.128.1") == True
        assert pycat.ipCheck("1.1.128.254") == True
        assert pycat.ipCheck("223.254.128.1") == True
        assert pycat.ipCheck("223.1.128.254") == True
        assert pycat.ipCheck("1.254.128.254") == True
        assert pycat.ipCheck("223.254.128.254") == True

        assert pycat.ipCheck("1.128.1.1") == True
        assert pycat.ipCheck("223.128.1.1") == True
        assert pycat.ipCheck("1.128.254.1") == True
        assert pycat.ipCheck("1.128.1.254") == True
        assert pycat.ipCheck("223.128.254.1") == True
        assert pycat.ipCheck("223.128.1.254") == True
        assert pycat.ipCheck("1.128.254.254") == True
        assert pycat.ipCheck("223.128.254.254") == True

        assert pycat.ipCheck("128.1.1.1") == True
        assert pycat.ipCheck("128.254.1.1") == True
        assert pycat.ipCheck("128.1.254.1") == True
        assert pycat.ipCheck("128.1.1.254") == True
        assert pycat.ipCheck("128.254.254.1") == True
        assert pycat.ipCheck("128.254.1.254") == True
        assert pycat.ipCheck("128.1.254.254") == True
        assert pycat.ipCheck("128.254.254.254") == True

        assert pycat.ipCheck("1.1.1.1") == True
        assert pycat.ipCheck("223.1.1.1") == True
        assert pycat.ipCheck("1.254.1.1") == True
        assert pycat.ipCheck("1.1.254.1") == True
        assert pycat.ipCheck("1.1.1.254") == True
        assert pycat.ipCheck("223.254.1.1") == True
        assert pycat.ipCheck("223.1.254.1") == True
        assert pycat.ipCheck("223.1.1.254") == True
        assert pycat.ipCheck("1.254.254.1") == True
        assert pycat.ipCheck("1.254.1.254") == True
        assert pycat.ipCheck("1.1.254.254") == True
        assert pycat.ipCheck("223.254.254.1") == True
        assert pycat.ipCheck("223.254.1.254") == True
        assert pycat.ipCheck("223.1.254.254") == True
        assert pycat.ipCheck("1.254.254.254") == True
        assert pycat.ipCheck("223.254.254.254") == True

    def test_StrongRobust(self):
        assert pycat.ipCheck("0.0.128.128") == False
        assert pycat.ipCheck("0.255.128.128") == False
        assert pycat.ipCheck("224.0.128.128") == False
        assert pycat.ipCheck("224.255.128.128") == False

        assert pycat.ipCheck("0.128.0.128") == False
        assert pycat.ipCheck("0.128.255.128") == False
        assert pycat.ipCheck("224.128.0.128") == False
        assert pycat.ipCheck("224.128.255.128") == False

        assert pycat.ipCheck("0.128.128.0") == False
        assert pycat.ipCheck("0.128.128.255") == False
        assert pycat.ipCheck("224.128.128.0") == False
        assert pycat.ipCheck("224.128.128.255") == False

        assert pycat.ipCheck("128.0.0.128") == False
        assert pycat.ipCheck("128.0.255.128") == False
        assert pycat.ipCheck("128.255.0.128") == False
        assert pycat.ipCheck("128.255.255.128") == False

        assert pycat.ipCheck("128.0.128.0") == False
        assert pycat.ipCheck("128.0.128.255") == False
        assert pycat.ipCheck("128.255.128.0") == False
        assert pycat.ipCheck("128.255.128.255") == False

        assert pycat.ipCheck("128.128.0.0") == False
        assert pycat.ipCheck("128.128.0.255") == False
        assert pycat.ipCheck("128.128.255.0") == False
        assert pycat.ipCheck("128.128.255.255") == False

        assert pycat.ipCheck("0.0.0.128") == False
        assert pycat.ipCheck("224.0.0.128") == False
        assert pycat.ipCheck("0.255.0.128") == False
        assert pycat.ipCheck("0.0.255.128") == False
        assert pycat.ipCheck("224.255.0.128") == False
        assert pycat.ipCheck("224.0.255.128") == False
        assert pycat.ipCheck("0.255.255.128") == False
        assert pycat.ipCheck("224.255.255.128") == False

        assert pycat.ipCheck("0.0.128.0") == False
        assert pycat.ipCheck("224.0.128.0") == False
        assert pycat.ipCheck("0.255.128.0") == False
        assert pycat.ipCheck("0.0.128.255") == False
        assert pycat.ipCheck("224.255.128.0") == False
        assert pycat.ipCheck("224.0.128.255") == False
        assert pycat.ipCheck("0.255.128.255") == False
        assert pycat.ipCheck("224.255.128.255") == False

        assert pycat.ipCheck("0.128.0.0") == False
        assert pycat.ipCheck("224.128.0.0") == False
        assert pycat.ipCheck("0.128.255.0") == False
        assert pycat.ipCheck("0.128.0.255") == False
        assert pycat.ipCheck("224.128.255.0") == False
        assert pycat.ipCheck("224.128.0.255") == False
        assert pycat.ipCheck("0.128.255.255") == False
        assert pycat.ipCheck("224.128.255.255") == False

        assert pycat.ipCheck("128.0.0.0") == False
        assert pycat.ipCheck("128.255.0.0") == False
        assert pycat.ipCheck("128.0.255.0") == False
        assert pycat.ipCheck("128.0.0.255") == False
        assert pycat.ipCheck("128.255.255.0") == False
        assert pycat.ipCheck("128.255.0.255") == False
        assert pycat.ipCheck("128.0.255.255") == False
        assert pycat.ipCheck("128.255.255.255") == False

        assert pycat.ipCheck("0.0.0.0") == False
        assert pycat.ipCheck("224.0.0.0") == False
        assert pycat.ipCheck("0.255.0.0") == False
        assert pycat.ipCheck("0.0.255.0") == False
        assert pycat.ipCheck("0.0.0.255") == False
        assert pycat.ipCheck("224.255.0.0") == False
        assert pycat.ipCheck("224.0.255.0") == False
        assert pycat.ipCheck("224.0.0.255") == False
        assert pycat.ipCheck("0.255.255.0") == False
        assert pycat.ipCheck("0.255.0.255") == False
        assert pycat.ipCheck("0.0.255.255") == False
        assert pycat.ipCheck("224.255.255.0") == False
        assert pycat.ipCheck("224.255.0.255") == False
        assert pycat.ipCheck("224.0.255.255") == False
        assert pycat.ipCheck("0.255.255.255") == False
        assert pycat.ipCheck("224.255.255.255") == False

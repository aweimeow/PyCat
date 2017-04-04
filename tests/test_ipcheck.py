from PyCat import pycat

class TestBoundaryValue:
    def test_WeakNormal(self):
        assert pycat.ipCheck("0.128.128.128") == True
        assert pycat.ipCheck("255.128.128.128") == True

        assert pycat.ipCheck("128.0.128.128") == True
        assert pycat.ipCheck("128.255.128.128") == True
        
        assert pycat.ipCheck("128.128.0.128") == True
        assert pycat.ipCheck("128.128.255.128") == True
        
        assert pycat.ipCheck("128.128.128.0") == True
        assert pycat.ipCheck("128.128.128.255") == True

    def test_WeakRobust(self):
        assert pycat.ipCheck("-1.128.128.128") == False
        assert pycat.ipCheck("256.128.128.128") == False

        assert pycat.ipCheck("128.-1.128.128") == False
        assert pycat.ipCheck("128.256.128.128") == False

        assert pycat.ipCheck("128.128.-1.128") == False
        assert pycat.ipCheck("128.128.256.128") == False

        assert pycat.ipCheck("128.128.128.-1") == False
        assert pycat.ipCheck("128.128.128.256") == False

    def test_StrongNormal(self):
        assert pycat.ipCheck("0.0.128.128") == True
        assert pycat.ipCheck("0.255.128.128") == True
        assert pycat.ipCheck("255.0.128.128") == True
        assert pycat.ipCheck("255.255.128.128") == True

        assert pycat.ipCheck("0.128.0.128") == True
        assert pycat.ipCheck("0.128.255.128") == True
        assert pycat.ipCheck("255.128.0.128") == True
        assert pycat.ipCheck("255.128.255.128") == True

        assert pycat.ipCheck("0.128.128.0") == True
        assert pycat.ipCheck("0.128.128.255") == True
        assert pycat.ipCheck("255.128.128.0") == True
        assert pycat.ipCheck("255.128.128.255") == True

        assert pycat.ipCheck("128.0.0.128") == True
        assert pycat.ipCheck("128.0.255.128") == True
        assert pycat.ipCheck("128.255.0.128") == True
        assert pycat.ipCheck("128.255.255.128") == True

        assert pycat.ipCheck("128.0.128.0") == True
        assert pycat.ipCheck("128.0.128.255") == True
        assert pycat.ipCheck("128.255.128.0") == True
        assert pycat.ipCheck("128.255.128.255") == True

        assert pycat.ipCheck("128.128.0.0") == True
        assert pycat.ipCheck("128.128.0.255") == True
        assert pycat.ipCheck("128.128.255.0") == True
        assert pycat.ipCheck("128.128.255.255") == True

        assert pycat.ipCheck("0.0.0.128") == True
        assert pycat.ipCheck("255.0.0.128") == True
        assert pycat.ipCheck("0.255.0.128") == True
        assert pycat.ipCheck("0.0.255.128") == True
        assert pycat.ipCheck("255.255.0.128") == True
        assert pycat.ipCheck("255.0.255.128") == True
        assert pycat.ipCheck("0.255.255.128") == True
        assert pycat.ipCheck("255.255.255.128") == True

        assert pycat.ipCheck("0.0.128.0") == True
        assert pycat.ipCheck("255.0.128.0") == True
        assert pycat.ipCheck("0.255.128.0") == True
        assert pycat.ipCheck("0.0.128.255") == True
        assert pycat.ipCheck("255.255.128.0") == True
        assert pycat.ipCheck("255.0.128.255") == True
        assert pycat.ipCheck("0.255.128.255") == True
        assert pycat.ipCheck("255.255.128.255") == True

        assert pycat.ipCheck("0.128.0.0") == True
        assert pycat.ipCheck("255.128.0.0") == True
        assert pycat.ipCheck("0.128.255.0") == True
        assert pycat.ipCheck("0.128.0.255") == True
        assert pycat.ipCheck("255.128.255.0") == True
        assert pycat.ipCheck("255.128.0.255") == True
        assert pycat.ipCheck("0.128.255.255") == True
        assert pycat.ipCheck("255.128.255.255") == True

        assert pycat.ipCheck("128.0.0.0") == True
        assert pycat.ipCheck("128.255.0.0") == True
        assert pycat.ipCheck("128.0.255.0") == True
        assert pycat.ipCheck("128.0.0.255") == True
        assert pycat.ipCheck("128.255.255.0") == True
        assert pycat.ipCheck("128.255.0.255") == True
        assert pycat.ipCheck("128.0.255.255") == True
        assert pycat.ipCheck("128.255.255.255") == True

        assert pycat.ipCheck("0.0.0.0") == True
        assert pycat.ipCheck("255.0.0.0") == True
        assert pycat.ipCheck("0.255.0.0") == True
        assert pycat.ipCheck("0.0.255.0") == True
        assert pycat.ipCheck("0.0.0.255") == True
        assert pycat.ipCheck("255.255.0.0") == True
        assert pycat.ipCheck("255.0.255.0") == True
        assert pycat.ipCheck("255.0.0.255") == True
        assert pycat.ipCheck("0.255.255.0") == True
        assert pycat.ipCheck("0.255.0.255") == True
        assert pycat.ipCheck("0.0.255.255") == True
        assert pycat.ipCheck("255.255.255.0") == True
        assert pycat.ipCheck("255.255.0.255") == True
        assert pycat.ipCheck("255.0.255.255") == True
        assert pycat.ipCheck("0.255.255.255") == True
        assert pycat.ipCheck("255.255.255.255") == True

    def test_StrongRobust(self):
        assert pycat.ipCheck("-1.-1.128.128") == False
        assert pycat.ipCheck("-1.256.128.128") == False
        assert pycat.ipCheck("256.-1.128.128") == False
        assert pycat.ipCheck("256.256.128.128") == False

        assert pycat.ipCheck("-1.128.-1.128") == False
        assert pycat.ipCheck("-1.128.256.128") == False
        assert pycat.ipCheck("256.128.-1.128") == False
        assert pycat.ipCheck("256.128.256.128") == False

        assert pycat.ipCheck("-1.128.128.-1") == False
        assert pycat.ipCheck("-1.128.128.256") == False
        assert pycat.ipCheck("256.128.128.-1") == False
        assert pycat.ipCheck("256.128.128.256") == False

        assert pycat.ipCheck("128.-1.-1.128") == False
        assert pycat.ipCheck("128.-1.256.128") == False
        assert pycat.ipCheck("128.256.-1.128") == False
        assert pycat.ipCheck("128.256.256.128") == False

        assert pycat.ipCheck("128.-1.128.-1") == False
        assert pycat.ipCheck("128.-1.128.256") == False
        assert pycat.ipCheck("128.256.128.-1") == False
        assert pycat.ipCheck("128.256.128.256") == False

        assert pycat.ipCheck("128.128.-1.-1") == False
        assert pycat.ipCheck("128.128.-1.256") == False
        assert pycat.ipCheck("128.128.256.-1") == False
        assert pycat.ipCheck("128.128.256.256") == False

        assert pycat.ipCheck("-1.-1.-1.128") == False
        assert pycat.ipCheck("256.-1.-1.128") == False
        assert pycat.ipCheck("-1.256.-1.128") == False
        assert pycat.ipCheck("-1.-1.256.128") == False
        assert pycat.ipCheck("256.256.-1.128") == False
        assert pycat.ipCheck("256.-1.256.128") == False
        assert pycat.ipCheck("-1.256.256.128") == False
        assert pycat.ipCheck("256.256.256.128") == False

        assert pycat.ipCheck("-1.-1.128.-1") == False
        assert pycat.ipCheck("256.-1.128.-1") == False
        assert pycat.ipCheck("-1.256.128.-1") == False
        assert pycat.ipCheck("-1.-1.128.256") == False
        assert pycat.ipCheck("256.256.128.-1") == False
        assert pycat.ipCheck("256.-1.128.256") == False
        assert pycat.ipCheck("-1.256.128.256") == False
        assert pycat.ipCheck("256.256.128.256") == False

        assert pycat.ipCheck("-1.128.-1.-1") == False
        assert pycat.ipCheck("256.128.-1.-1") == False
        assert pycat.ipCheck("-1.128.256.-1") == False
        assert pycat.ipCheck("-1.128.-1.256") == False
        assert pycat.ipCheck("256.128.256.-1") == False
        assert pycat.ipCheck("256.128.-1.256") == False
        assert pycat.ipCheck("-1.128.256.256") == False
        assert pycat.ipCheck("256.128.256.256") == False

        assert pycat.ipCheck("128.-1.-1.-1") == False
        assert pycat.ipCheck("128.256.-1.-1") == False
        assert pycat.ipCheck("128.-1.256.-1") == False
        assert pycat.ipCheck("128.-1.-1.256") == False
        assert pycat.ipCheck("128.256.256.-1") == False
        assert pycat.ipCheck("128.256.-1.256") == False
        assert pycat.ipCheck("128.-1.256.256") == False
        assert pycat.ipCheck("128.256.256.256") == False

        assert pycat.ipCheck("-1.-1.-1.-1") == False
        assert pycat.ipCheck("256.-1.-1.-1") == False
        assert pycat.ipCheck("-1.256.-1.-1") == False
        assert pycat.ipCheck("-1.-1.256.-1") == False
        assert pycat.ipCheck("-1.-1.-1.256") == False
        assert pycat.ipCheck("256.256.-1.-1") == False
        assert pycat.ipCheck("256.-1.256.-1") == False
        assert pycat.ipCheck("256.-1.-1.256") == False
        assert pycat.ipCheck("-1.256.256.-1") == False
        assert pycat.ipCheck("-1.256.-1.256") == False
        assert pycat.ipCheck("-1.-1.256.256") == False
        assert pycat.ipCheck("256.256.256.-1") == False
        assert pycat.ipCheck("256.256.-1.256") == False
        assert pycat.ipCheck("256.-1.256.256") == False
        assert pycat.ipCheck("-1.256.256.256") == False
        assert pycat.ipCheck("256.256.256.256") == False

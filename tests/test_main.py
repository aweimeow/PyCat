# ip range 0.0.0.0 to 255.255.255.255
# port range 0 to 65535
# option:
# -h: help
# -t: target ip, eg: 192.168.0.1 or 192.168.0.1/24 or 192.168.0.1/255.255.255.0
# -p: the port of target ip
# -c: command eg: ls
import json
from PyCat import pycat
pycat.F_SCAN = False


class TestNormalBoundary:
    def test_normal(self):
        """ IP part """
        """one IP and one Port """
        assert json.loads(pycat.main("0.0.0.0", "17768"))["success"]  # min
        assert json.loads(pycat.main("0.0.0.1", "17768"))["success"]  # min+1
        # max-1
        assert json.loads(pycat.main("255.255.255.254", "17768"))["success"]
        # max
        assert json.loads(pycat.main("255.255.255.255", "17768"))["success"]
        """ Subnet and one Port """
        assert json.loads(pycat.main("0.0.0.0/16", "17768"))["success"]  # min
        # min+1
        assert json.loads(pycat.main("0.0.0.1/16", "17768"))["success"]
        # max-1
        assert json.loads(pycat.main("255.255.255.254/16", "17768"))["success"]
        # max
        assert json.loads(pycat.main("255.255.255.255/16", "17768"))["success"]
        """ Subnet """
        """ Subnet and one Port """
        # min
        assert json.loads(pycat.main("128.128.128.128/0", "17768"))["success"]
        # min+1
        assert json.loads(pycat.main("128.128.128.128/1", "17768"))["success"]
        # max-1
        assert json.loads(pycat.main("128.128.128.128/31", "17768"))["success"]
        # max
        assert json.loads(pycat.main("128.128.128.128/32", "17768"))["success"]
        """ Port part """
        """one IP and one Port """
        assert json.loads(pycat.main("128.128.128.128", "0"))["success"]  # min
        # min+1
        assert json.loads(pycat.main("128.128.128.128", "1"))["success"]
        # max-1
        assert json.loads(pycat.main("128.128.128.128", "65534"))["success"]
        # max
        assert json.loads(pycat.main("128.128.128.128", "65535"))["success"]
        """ Subnet and one Port """
        # min
        assert json.loads(pycat.main("128.128.128.128/16", "0"))["success"]
        # min+1
        assert json.loads(pycat.main("128.128.128.128/16", "1"))["success"]
        # max-1
        assert json.loads(pycat.main("128.128.128.128/16", "65534"))["success"]
        # max
        assert json.loads(pycat.main("128.128.128.128/16", "65535"))["success"]
        """ All middle """
        assert json.loads(pycat.main("128.128.128.128", "17768"))["success"]
        assert json.loads(pycat.main("128.128.128.128/16", "17768"))["success"]


class TestEquivalence:
    """ Normal Equivalence Class """
    def test_Normal(self):
        """ Weak Normal & Strong Normal Equivalence Class """
        assert json.loads(pycat.main("128.128.128.128", "17768"))["success"]
        assert json.loads(pycat.main("128.128.128.128/16", "17768"))["success"]

    """ Robust Equivalence Class """
    def test_Robust(self):
        """ Weak & Strong Robust Equivalence Class """
        """ IP part """
        # min - 1
        assert not json.loads(pycat.main("-1.255.255.255", "17768"))["success"]
        assert not json.loads(pycat.main(
            "-1.255.255.255/16", "17768"))["success"]
        # max + 1
        assert not json.loads(pycat.main(
            "255.255.255.256", "17768"))["success"]
        assert not json.loads(pycat.main(
            "255.255.255.256/16", "17768"))["success"]
        """ Submask part """
        # min - 1
        assert not json.loads(pycat.main(
            "128.128.128.128/-1", "17768"))["success"]
        # max + 1
        assert not json.loads(pycat.main(
            "128.128.128.128/33", "17768"))["success"]
        """ Port """
        # min - 1
        assert not json.loads(pycat.main("128.128.128.128", "-1"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128/16", "-1"))["success"]
        # max + 1
        assert not json.loads(pycat.main(
            "128.128.128.128", "65536"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128/16", "65536"))["success"]
        """ Strong Robust Equivalence Class """
        """ IP and subnet """
        assert not json.loads(pycat.main(
            "-1.255.255.255/-1", "17768"))["success"]
        assert not json.loads(pycat.main(
            "255.255.255.256/33", "17768"))["success"]
        """ submask and port """
        assert not json.loads(pycat.main(
            "128.128.128.128/-1", "-1"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128/33", "65536"))["success"]
        """ ip and port """
        # min - 1
        assert not json.loads(pycat.main("-1.255.255.255", "-1"))["success"]
        assert not json.loads(pycat.main("-1.255.255.255/16", "-1"))["success"]
        # max + 1
        assert not json.loads(pycat.main(
            "255.255.255.256", "65536"))["success"]
        assert not json.loads(pycat.main(
            "255.255.255.256/16", "65536"))["success"]
        """ All """
        assert not json.loads(pycat.main("-1.255.255.255/-1", "-1"))["success"]
        assert not json.loads(pycat.main(
            "255.255.255.256/32", "65536"))["success"]


class TestDecisionTable:
    """ normal format """
    def test_normal(self):
        assert json.loads(pycat.main("128.128.128.128", "17768"))["success"]
        assert json.loads(pycat.main("128.128.128.128/16", "17768"))["success"]
        assert json.loads(pycat.main(
            "128.128.128.128", "22,80,443"))["success"]
        assert json.loads(pycat.main("128.128.128.128/16", "22-25"))["success"]

    """ abnormal format """
    def test_RuleB(self):
        assert not json.loads(pycat.main("128.128.128", "17768"))["success"]
        assert not json.loads(pycat.main("128,128,128,128", "22"))["success"]
        assert not json.loads(pycat.main("128,128.128,128", "22"))["success"]
        assert not json.loads(pycat.main(
            "128,128,128,128", "22~25"))["success"]
        assert not json.loads(pycat.main("128-128-128-128", "22"))["success"]
        assert not json.loads(pycat.main("128/128/128/128", "22"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128", "22.80"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128", "22,80.443"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128", "22/80.443"))["success"]
        assert not json.loads(pycat.main(
            "128.128.128.128", "128.128.128.128"))["success"]
        assert not json.loads(pycat.main("128", "128.128.128.128"))["success"]

    """ unusual format """
    def test_RuleC(self):
        assert not json.loads(pycat.main("Ops", "Ops"))["success"]
        assert not json.loads(pycat.main("none", "none"))["success"]
        assert not json.loads(pycat.main("Null", "Null"))["success"]
        assert not json.loads(pycat.main(";--", "#"))["success"]

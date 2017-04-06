# ip range 0.0.0.0 to 255.255.255.255
# port range 0 to 65535
# option:
# -h: help
# -t: target ip, eg: 192.168.0.1 or 192.168.0.1/24 or 192.168.0.1/255.255.255.0
# -p: the port of target ip
# -c: command eg: ls
import json
from PyCat import pycat


class DecisionTable:
    """ normal format """
    def test_normal(self):
        """ only option """
        assert json.load(pycat.main("-h"))["success"]
        """ option with -t """
        assert not json.load(pycat.main("-t"))["success"]
        assert json.load(pycat.main("-t 128.128.128.128"))["success"]
        assert json.load(pycat.main("-t 128.128.128.128/16"))["success"]
        """ option with -t -p """
        assert not json.load(pycat.main("-t 128.128.128.128 -p"))["success"]
        assert json.load(pycat.main("-t 128.128.128.128 -p 17768"))["success"]
        assert json.load(pycat.main("-p 17768 -t 128.128.128.128"))["success"]
        assert not json.load(pycat.main("-t 128.128.128.128/16 -p"))["success"]
        assert json.load(pycat.main(
            "-t 128.128.128.128/16 -p 17768"))["success"]
        assert json.load(pycat.main(
            "-p 17768 -t 128.128.128.128/16"))["success"]
        assert not json.load(pycat.main("-t -p 17768"))["success"]
        assert not json.load(pycat.main("-t -p"))["success"]
        """ option with -t -c """
        assert not json.load(pycat.main("-t 128.128.128.128 -c"))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-c echo\"HiPycat\" -t 128.128.128.128"))["success"]
        assert not json.load(pycat.main("-t 128.128.128.128/16 -c"))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128/16 -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-c echo\"HiPycat\" -t 128.128.128.128/16"))["success"]
        assert not json.load(pycat.main("-t -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main("-t -c"))["success"]
        """ option with -p -c """
        assert not json.load(pycat.main("-p 17768 -c"))["success"]
        assert not json.load(pycat.main(
            "-p 17768 -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-c echo\"HiPycat\" -p 17768"))["success"]
        assert not json.load(pycat.main("-p -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main("-p -c"))["success"]
        """ option with -t -p -c """
        assert not json.load(pycat.main(
            "-t -p 17768 -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p 17768 -c"))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128/16 -p -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128/16 -p 17768 -c"))["success"]
        assert not json.load(pycat.main("-t -p -c echo\"HiPycat\""))["success"]
        assert not json.load(pycat.main("-t 128.128.128.128 -p -c"))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128/16 -p -c"))["success"]
        assert not json.load(pycat.main("-t -p 17768 -c"))["success"]
        assert not json.load(pycat.main("-t -p -c"))["success"]
        assert json.load(pycat.main(
            "-t 128.128.128.128 -p 17768 -c echo\"HiPycat\""))["success"]
        assert json.load(pycat.main(
            "-t 128.128.128.128 -c echo\"HiPycat\" -p 17768"))["success"]
        assert json.load(pycat.main(
            "-p 17768 -c echo\"HiPycat\" -t 128.128.128.128"))["success"]
        assert json.load(pycat.main(
            "-p 17768 -t 128.128.128.128 -c echo\"HiPycat\""))["success"]
        assert json.load(pycat.main(
            "-c echo\"HiPycat\" -t 128.128.128.128 -p 17768"))["success"]
        assert json.load(pycat.main(
            "-c echo\"HiPycat\" -p 17768 -t 128.128.128.128"))["success"]
        assert json.load(pycat.main(
            "-t 128.128.128.128/16 -p 17768 -c echo\"HiPycat\""))["success"]
        assert json.load(pycat.main(
            "-t 128.128.128.128/16 -c echo\"HiPycat\" -p 17768"))["success"]
        assert json.load(pycat.main(
            "-p 17768 -c echo\"HiPycat\" -t 128.128.128.128/16"))["success"]
        assert json.load(pycat.main(
            "-p 17768 -t 128.128.128.128/16 -c echo\"HiPycat\""))["success"]
        assert json.load(pycat.main(
            "-c echo\"HiPycat\" -t 128.128.128.128/16 -p 17768"))["success"]
        assert json.load(pycat.main(
            "-c echo\"HiPycat\" -p 17768 -t 128.128.128.128/16"))["success"]

    """ ip, port, option not in range """
    def test_RuleB(self):
        """ only options """
        assert not json.load(pycat.main("-1"))["success"]  # number
        assert not json.load(pycat.main("-z"))["success"]  # not in option list
        assert not json.load(pycat.main("-t -p"))["success"]
        assert not json.load(pycat.main("-t -p -c"))["success"]
        """ option with -t """
        # not in range number
        assert not json.load(pycat.main("-t -1.0.0.0"))["success"]
        assert not json.load(pycat.main("-t 255.255.255.256"))["success"]
        assert not json.load(pycat.main("-t 128.128.128.128/-1"))["success"]
        assert not json.load(pycat.main("-t 128.128.128.128/33"))["success"]
        assert not json.load(pycat.main("-t -1.0.0.0/-1"))["success"]
        assert not json.load(pycat.main("-t 255.255.255.256/33"))["success"]
        """ option with -t -p """
        assert not json.load(pycat.main("-t -1.0.0.0 -p 17768"))["success"]
        # ip not in range number
        assert not json.load(pycat.main(
            "-t 255.255.255.256 -p 17768"))["success"]
        # port not in range number
        assert not json.load(pycat.main("-t 128.128.128.128 -p -1"))["success"]
        # port not in range number
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p 65536"))["success"]
        # ip and port both not in range number
        assert not json.load(pycat.main("-t -1.0.0.0 -p 65536"))["success"]

    """ abnormal format """
    def test_RuleC(self):
        """ only option """
        assert not json.load(pycat.main("Ops"))["success"]  # string
        """ option with -t """
        # number and comma
        assert not json.load(pycat.main("-t 128,128,128,128"))["success"]
        # number and dash
        assert not json.load(pycat.main("-t 128-128-128-128"))["success"]
        # number, dot and comma
        assert not json.load(pycat.main("-t 128.128,128,128"))["success"]
        # string and dot
        assert not json.load(pycat.main("-t aaa.bbb.ccc.ddd"))["success"]
        # string and comma
        assert not json.load(pycat.main("-t aaa,bbb,ccc,ddd"))["success"]
        # number, dot and comma
        assert not json.load(pycat.main("-t aaa.bbb,ccc,ddd"))["success"]
        # number, string, dot
        assert not json.load(pycat.main("-t 128.bbb.128.ddd"))["success"]
        # number, string, dot and comma
        assert not json.load(pycat.main("-t 128.bbb,ccc,ddd"))["success"]
        """ option with -t -p """
        # ip is abnormal, port normal
        assert not json.load(pycat.main(
            "-t 128,128,128,128 -p 17768"))["success"]
        # number, dot and comma
        assert not json.load(pycat.main(
            "-t 128.128,128,128 -p 17768"))["success"]
        # string and dot
        assert not json.load(pycat.main(
            "-t aaa.bbb.ccc.ddd -p 17768"))["success"]
        # string and comma
        assert not json.load(pycat.main(
            "-t aaa,bbb,ccc,ddd -p 17768"))["success"]
        # number, dot and comma
        assert not json.load(pycat.main(
            "-t aaa.bbb,ccc,ddd -p 17768"))["success"]
        # number, string, dot
        assert not json.load(pycat.main(
            "-t 128.bbb.128.ddd -p 17768"))["success"]
        # number, string, dot and comma
        assert not json.load(pycat.main(
            "-t 128.bbb,ccc,ddd -p 17768"))["success"]
        # ip is normal, port is abnormal
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p myport"))["success"]  # string
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p none"))["success"]  # none
        assert not json.load(pycat.main(
            "-t 128.128.128.128 -p ."))["success"]  # dot
        # ip and port are abnormal
        assert not json.load(pycat.main(
            "-t 128,128,128,128 -p myport"))["success"]  # string
        assert not json.load(pycat.main(
            "-t 128.aaa.128.128 -p none"))["success"]  # none

    """ unusual format """
    def test_RuleD(self):
        assert not json.load(pycat.main("abc 123"))["success"]
        assert not json.load(pycat.main(
            "-t 128.128.128.128, -p 17768, -c echo\"HiPycat\""))["success"]

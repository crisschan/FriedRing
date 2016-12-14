#!/usr/bin/env python
# coding=utf-8
import getopt
import os
import time
import sys
from mitmproxy import proxy
from FriedRing import FriedRing
from alasRun import alasRun

VERSION = '2.0.1'


def main():
    opts, args = getopt.getopt(sys.argv[1:], "hpr:w:")
    strPort = 8888
    fnamescript = '__crisschan_TEMP' + str(time.time())
    for op, value in opts:
        if op == "-p":
            strPort = value
        elif op == "-w":
            fnamescript = value
        elif op == "-r":
            sTargetRun = value
        elif op == "-h":
            # usage()
            print '-p the proxy port\r\n-r the run all scenario under test workspace,the param is:\r\n    s - is serial run all scenrio \r\n    p - is parralle run all scenrio\r\n-w the performance test workspace name \r\n'
            sys.exit()

    config = proxy.ProxyConfig(
        cadir=os.path.expanduser("~/.mitmproxy/"),
        port=int(strPort)
    )

    if op == '-r':
        ARun = alasRun()
        if sTargetRun == 's':
            ARun.sRun()
        elif sTargetRun == 'p':
            ARun.pRun()
        else:
            print '-r is the error input!!!!'
            return 0
    else:
        server = proxy.ProxyServer(config)
        print 'the porxy port is ' + str(strPort)
        m = FriedRing(server, fnamescript)
        m.run()


if __name__ == "__main__":
    main()

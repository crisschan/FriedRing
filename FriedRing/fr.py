#!/usr/bin/env python
#coding=utf-8
import getopt
import os
import time
import sys
from mitmproxy import controller
from mitmproxy import proxy
from mitmproxy.controller import Master
from FriedRing import FriedRing

VERSION='1.0.10'
def main():

    opts, args = getopt.getopt(sys.argv[1:], "hp:w:")
    strPort=8888
    fnamescript='__crisschan_TEMP'+str(time.time())
    for op, value in opts:
        if op == "-p":
            strPort = value
        elif op == "-w":
            fnamescript = value
        elif op == "-h":
            #usage()
            print '-p the proxy port\r\n-w the script_solution  name'
            sys.exit()


    config = proxy.ProxyConfig(
        cadir=os.path.expanduser("~/.mitmproxy/"),
        port=int(strPort)
    )


    server = proxy.ProxyServer(config)
    print 'the porxy port is '+str(strPort)
    m = FriedRing(server, fnamescript)
    m.run()
if __name__ == "__main__":
    main()
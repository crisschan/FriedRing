#!/usr/bin/env python
#coding=utf-8
import getopt
import os
import time
#import shutil
#import subprocess
import sys
#import optparse

from mitmproxy import proxy

from FriedRing import FriedRing

VERSION='1.0.5'
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
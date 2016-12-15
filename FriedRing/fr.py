#!/usr/bin/env python
# coding=utf-8
import getopt
import os
import time
import sys
import types
from mitmproxy import proxy
from FriedRing import FriedRing
from alasRun import alasRun

VERSION = '2.0.5'
#run_time = 30,rampup = 0,results_ts_interval = 1,progress_bar = 'on',console_logging = 'on',xml_report = 'off',threads = 10):

def main():
    opts, args = getopt.getopt(sys.argv[1:], "hp:w:r:t:u:i:b:c:x:v:",
                               ["help","proxyport=", "workspace=","run=","runtime=","rampup=","resultinterval=","progressbar=","consolelogging=","xmlreport=","vusers="])
    strPort = 8888
    fnamescript = '__crisschan_TEMP' + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    op=''
    sTargetRun='c'
    run_time = 30
    rampup = 0
    results_ts_interval = 1
    progress_bar = 'on'
    console_logging = 'on'
    xml_report = 'off'
    threads = 10
    for op, value in opts:
        if op in ("-p","--proxyport"):
            strPort = value
        elif op in ("-w","--workspace"):
            fnamescript = value
        elif op in ("-r","--run"):
            sTargetRun = value
        elif op in ('-t',"--runtime"):
            try:
                run_time =int(value)
            except:
                print 'run_time must is int!'
                return 0
        elif op in ("-u","--rampup"):
            try:
                rampup=int(value)
            except:
                print 'rampup must is int!'
                return 0
        elif op in ("-i","--resultinterval"):
            try:
                results_ts_interval=int(value)
            except:
                print 'results_ts_interval must is int!'
                return 0
        elif op in ("-b","--progressbar"):
            progress_bar=value
        elif op in ("-c","--consolelogging"):
            console_logging=value
        elif op in ("-x","--xmlreport"):
            xml_report=value
        elif op in ("-v","--vusers"):
            try:
                threads=int(value)
            except:
                print 'threads must is int!'
                return 0
        elif op in ("-h","--help"):
            # usage()
            print '-p the proxy port\r\n' \
                  '-r the run all scenario under test workspace,the param is:\r\n' \
                  '    s - is serial run all scenrio \r\n' \
                  '    p - is parralle run all scenrio\r\n' \
                  '-w the performance test workspace name \r\n\r\n' \
                  'other is the scenrio config seting that is available for parralle run:\r\n' \
                  '    -t is runtime that duration of test (seconds)\r\n' \
                  '    -u is rampup that duration of user rampup\r\n' \
                  '    -i is resultinterval that time series interval for results analysis (seconds) \r\n' \
                  '    -b is progressbar that turn on/off console progress bar during test run default = on\r\n' \
                  '    -c is consolelogging that turn on/off logging to stdout default = on\r\n' \
                  '    -x is xmlreport that turn on/off xml/jtl report default = off\r\n' \
                  '    -v is vusers that number of threads/virtual users default=10\r\n'

            sys.exit()

    config = proxy.ProxyConfig(
        cadir=os.path.expanduser("~/.mitmproxy/"),
        port=int(strPort)
    )
    print run_time,rampup,results_ts_interval,progress_bar,console_logging,xml_report,threads
    if sTargetRun != 'c':
        ARun = alasRun()
        if sTargetRun == 's':
            ARun.sRun()
        elif sTargetRun == 'p':
            if type(run_time)!=type(1):
                print 'run_time must is int!'
                return 0
            if type(rampup)!=type(1):
                print 'rampup must is int!'
                return 0
            if type(results_ts_interval)!=type(1):
                print 'results_ts_interval must is int!'
                return 0
            if progress_bar!='on' and progress_bar!='off':
                print 'progress_bar only input on/off!'
                return 0
            if console_logging!='on' and console_logging!='off':
                print 'console_logging only input on/off!'
                return 0
            if xml_report!='on' and xml_report!='off':
                print 'xml_report only input on/off!'
                return 0
            if type(threads)!=type(1):
                print 'threads must is int!'
                return 0
            ARun.pRun(run_time,rampup,results_ts_interval,progress_bar,console_logging,xml_report,threads)
        else:
            print '-r is the error input!!!!'
            return 0
    else:
        server = proxy.ProxyServer(config)
        print 'the porxy port is ' + str(strPort)
        m = FriedRing(server, fnamescript)
        m.run()


    '''
    print strPort
    print  fnamescript
    print  op
    print  sTargetRun
    print run_time
    print rampup
    print results_ts_interval
    print progress_bar
    print console_logging
    print xml_report
    print threads
    '''

if __name__ == "__main__":
    main()

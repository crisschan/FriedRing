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
#from FRun import FRun
VERSION='1.0.0'
def main():
    opts, args = getopt.getopt(sys.argv[1:], "hpr:w:")
    strPort=8888
    fnamescript='__crisschan_TEMP'+str(time.time())

    try:
        for op, value in opts:
            #if op == "-r":

                FRun(str(value))
                break
            elif op == "-p":
                strPort = value
            elif op == "-w":
                fnamescript = value
            elif op == "-h":
                #usage()
                print '-p the proxy port\r\n-w the script_solution  name'
                sys.exit()
        else:

            config = proxy.ProxyConfig(
                cadir=os.path.expanduser("~/.mitmproxy/"),
                port=int(strPort)
            )
            server = proxy.ProxyServer(config)
            print 'the porxy port is '+str(strPort)
            m = FriedRing(server, fnamescript)
            m.run()
    except KeyboardInterrupt:
        m.shutdown()
    '''

    usage = 'Usage: %prog <project name> [options]'
    parser = optparse.OptionParser(usage=usage, version=VERSION)
    parser.add_option('-p', '--port', dest='port', type='int', help='listener port')
    parser.add_option('-w', '--script solution(workspace)',  help='script directory')
    cmd_opts, args = parser.parse_args()

    try:
        project_name = args[0]
    except IndexError:
        sys.stderr.write('\nERROR: no project specified\n\n')
        sys.stderr.write('%s\n' % usage)
        sys.stderr.write('Example: multimech-run my_project\n\n')
        sys.exit(1)

    core.init(cmd_opts.projects_dir, project_name)

    # -- ORIGINAL-MAIN:
    if cmd_opts.results_dir:  # don't run a test, just re-process results
        rerun_results(project_name, cmd_opts, cmd_opts.results_dir)
    elif cmd_opts.port:
        import multimechanize.rpcserver
        multimechanize.rpcserver.launch_rpc_server(cmd_opts.bind_addr, cmd_opts.port, project_name, run_test)
    else:
        run_test(project_name, cmd_opts)
    return
'''
if __name__ == "__main__":
    main()
#!/usr/bin/env python
# coding=utf-8
'''
author:Crisschan
time:2016-6-30
'''
from mitmproxy import controller, proxy
import os
import datetime
from F2requests import F2requests
from Cfg import Cfg


class FriedRing(controller.Master):
    # fscript =
    def __init__(self, server, fnamescript):
        curscenrioscript = fnamescript
        curpath = os.path.abspath(os.curdir)
        fscriptsolutionpath = os.path.join(curpath, fnamescript)
        if not os.path.isdir(fscriptsolutionpath):
            os.makedirs(fscriptsolutionpath)
        else:
            fnamescript = fnamescript + str(datetime.datetime.now().microsecond)
            fscriptsolutionpath = os.path.join(curpath, fnamescript)
            os.makedirs(fscriptsolutionpath)

        Cfg(fscriptsolutionpath, curscenrioscript)
        self.fnamescript = str(fscriptsolutionpath) + '/test_scripts/' + curscenrioscript + 'script.py'
        print 'script solution path(include script files, config files and results:' + str(fscriptsolutionpath)

        controller.Master.__init__(self, server)
        self.f2r = F2requests(self.fnamescript)

    # def shutdown(self):
    #   self.shutdown()
    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, msg):
        # print msg
        req = msg.request
        print str(req.host) + str(req.path)
        self.f2r.F2Req(req)
        msg.reply()

    def handle_response(self, msgg):
        # print msg
        msgg.reply()
        res = msgg.response
        '''
        print res.status_code
        print res.headers
        print res.content+'\n'
        print res.reason+'\n'
        print res.timestamp_start+'\n'
        print res.timestamp_end+'\n'
        print '--------------------------------------\n'
        '''


'''
if  __name__ == '__main__':
    opts = options.Options(cadir="~/.mitmproxy/", listen_port=8888)
    config = proxy.ProxyConfig(opts)
    server = proxy.ProxyServer(config)
    m = FriedRing(server,'/Users/chancriss/Desktop/WorkSpace/PythonSpace/FriedRingWorkSpace/')
    m.run()
'''

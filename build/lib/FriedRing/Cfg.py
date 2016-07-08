import os

class Cfg():
    def __init__(self,fscriptsolutionpath):
        self.fscriptsolutionpath=fscriptsolutionpath
        self.__Setcfg()
        self.__SetVU()
    def __Setcfg(self):
        fcfgpath = str(self.fscriptsolutionpath)+'/config.cfg'
        fcfg = open(fcfgpath,'w')
        scfglines = '[global]\r\nrun_time = 30\r\nrampup = 0\r\nresults_ts_interval = 1\r\nprogress_bar = on\r\nconsole_logging = on\r\nxml_report = off\r\n\r\n[user_group - 1]\r\nthreads = 1\r\nscript = v_user.py'
        fcfg.write(scfglines)
        fcfg.close()
    def __SetVU(self):
        fV_UserPath = os.path.join(self.fscriptsolutionpath,'test_scripts')
        if not os.path.isdir(fV_UserPath):
            os.makedirs(fV_UserPath)
        fV_Userfile = str(fV_UserPath)+'/v_user.py'
        fV_Userscript = open(fV_Userfile,'w')
        sScript = '#!/usr/bin/env python\r\n#coding=utf-8\r\nimport requests\r\nimport json\r\nimport time\r\nimport script\r\nclass Transaction(object):\r\n    def __init__(self):\r\n        #self.custom_timers={}\r\n        pass\r\n    def run(self):\r\n        #start_timer = time.time()\r\n        script.script()\r\n        #latency = time.time() - start_timer\r\n        #user\'s transaction \r\n        #self.custom_timers[\'Transaction_Custom\']=latency\r\nif __name__ == \'__main__\':\r\n    trans = Transaction()\r\n    trans.run()\r\n    #print trans.custom_timers'
        fV_Userscript.write(sScript)
        fV_Userscript.close()



# encoding=utf8
# !/usr/bin/python

import os
import subprocess
from Img2Base64 import Img2Base64
import time
import shutil


class alasRun(object):
    '''
    多场景的混合运行类，可以执行在test workspace下的全部测试场景，
    支持并发和线性执行两种模式
    this is a class for merge all performance testing scenario
     that scenario under the current test workspace dir
    '''

    def __init__(self):

        self.strCurPath = os.path.abspath(os.curdir)  # get the current work space

        self.scenariolist = []
        # self._collectReport()

        # self.startTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        # self.endTime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

    def _collectScenario(self):
        '''
        collect performance test scenario that under test workspace name
        Returns:
        null
        '''
        for root, dirs, files in os.walk(self.strCurPath):
            # print dirs

            for file in files:

                if file.find('script.py') >= 0 and root.find('Parralle_Scenario') < 0 and file[len(file) - 1] != 'c':
                    tempscenario = root[len(self.strCurPath):]
                    tempscenario = tempscenario[1:tempscenario.rfind('/')]
                    # print tempscenario
                    self.scenariolist.append(tempscenario)

    def _SerialReportIndex(self, ScenarioList, sResult):
        '''
        make the serial report index page
        Args:
            ScenarioList: scenario list
            sResult: the result dir

        Returns:

        '''
        wf = open(sResult + 'index.html', 'w')
        wf.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>Serial Report</title>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
    <meta http-equiv="Content-Language" content="en" />
    <style type="text/css">
        body {
            background-color: #FFFFFF;
            color: #000000;
            font-family: Verdana, sans-serif;
            font-size: 11px;
            padding: 5px;
        }
        h1 {
            font-size: 16px;
            background: #FF9933;
            margin-bottom: 0;
            padding-left: 5px;
            padding-top: 2px;
        }
        h2 {
            font-size: 13px;
            background: #C0C0C0;
            padding-left: 5px;
            margin-top: 2em;
            margin-bottom: .75em;
        }
        h3 {
            font-size: 12px;
            background: #EEEEEE;
            padding-left: 5px;
            margin-bottom: 0.5em;
        }
        h4 {
            font-size: 11px;
            padding-left: 20px;
            margin-bottom: 0;
        }
        p {
            margin: 0;
            padding: 0;
        }
        table {
            margin-left: 10px;
        }
        td {
            text-align: right;
            color: #000000;
            background: #FFFFFF;
            padding-left: 10px;
            padding-right: 10px;
            padding-bottom: 0;
        }
        th {
            text-align: center;
            padding-right: 10px;
            padding-left: 10px;
            color: #000000;
            background: #FFFFFF;
        }
        div.summary {
            padding-left: 20px;
        }
    </style>
</head>
<body>

<h1>Performance Results Report List</h1>

<h2>Summary</h2><div class="summary">''')
        wf.write('<b>test start:</b> ' + self.startTime + '<br /><br />')
        wf.write('<b>test finish:</b> ' + self.endTime + '<br /><br />')
        wf.write('''<h2>All Scenario </h2>
<h3>Detail</h3>
<table>
<tr><th>Scanrio Name </th><th>Report link</th></tr>
''')
        for Scenario in ScenarioList:
            wf.write(
                '<tr><td>' + Scenario + '</td><td><a href=\'' + Scenario + '.html\' target="_blank">' + Scenario + '</a></td></tr>')
        wf.write('''</table>
</body>
</html>''')
        wf.close()

    def _ImgtoHTMLBase(self, imgfile):
        sImgBase64 = ' <img src = "data:image/bmp;base64,' + Img2Base64(
            os.path.join(imgfile)).hexImg + '\"/>'
        return sImgBase64

    def _collectReport(self):
        '''
        this is a collection all scenrio report fun,and output the serial_result dir
        Returns:
        the report dir
        '''
        if not os.path.exists(self.strCurPath + '/Report/Serial_Result/'):
            os.makedirs(self.strCurPath + '/Report/Serial_Result/')
        sCurResult = self.strCurPath + '/Report/Serial_Result/Serial_Result' + time.strftime("%Y%m%d%H%M%S",
                                                                                             time.localtime(
                                                                                                 time.time())) + '/'

        os.makedirs(sCurResult)

        aTempReportList = []
        # aTempReportfilelist=[]
        for scenario in self.scenariolist:
            aTempstr = self.strCurPath + '/' + scenario + '/results/'
            for root, dirs, files in os.walk(aTempstr):
                for file in files:
                    if file == 'results.html':
                        # All_Transactions_response_times_intervals.png
                        # All_Transactions_response_times.png
                        # All_Transactions_throughput.png
                        reportfile = os.path.join(root, file)
                        rf = open(reportfile, 'r')
                        sResult = rf.read()
                        rf.close()
                        sbtimesintervals = self._ImgtoHTMLBase(
                            os.path.join(root, 'All_Transactions_response_times_intervals.png'))

                        sbtimes = self._ImgtoHTMLBase(os.path.join(root, 'All_Transactions_response_times.png'))
                        sthroughput = self._ImgtoHTMLBase(os.path.join(root, 'All_Transactions_throughput.png'))
                        sResult = sResult.replace('<img src="All_Transactions_response_times_intervals.png"></img>',
                                                  sbtimesintervals)
                        sResult = sResult.replace('<img src="All_Transactions_response_times.png"></img>',
                                                  sbtimes)
                        sResult = sResult.replace('<img src="All_Transactions_throughput.png"></img>',
                                                  sthroughput)
                        aTempReportList.append(scenario)

                        sTempResultfile = sCurResult + scenario + '.html'

                        wf = open(sTempResultfile, 'w')
                        wf.write(sResult)
                        wf.close()

        self._SerialReportIndex(aTempReportList, sCurResult)

    def _mvReport(self):

        sCurReport = self.strCurPath + '/Report/Parralle_Result/'

        sOldReport = self.strCurPath + '/Parralle_Scenario/results/'

        if os.path.exists(sCurReport):
            shutil.rmtree(sCurReport)
        shutil.copytree(sOldReport, sCurReport)

    def _clearHistoryScenrioResult(self):
        '''
        clear all scenrio history result
        Returns:

        '''
        for scenario in self.scenariolist:
            aTempstr = self.strCurPath + '/' + scenario + '/results/'
            if os.path.exists(aTempstr):
                shutil.rmtree(aTempstr)

    def sRun(self):
        '''
        serial process all scenario under test work space
        Returns:

        '''
        self.scenariolist = []
        self._collectScenario()
        if len(self.scenariolist) <= 0:
            print 'No Performance Test Scenario Under Current Test WorkSpace'
            return 0
        self._clearHistoryScenrioResult()

        i = 0
        self.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print '##Performance Test is running，Please wait!!'
        print 'Serial Run:'
        # print self.scenariolist

        for aline in self.scenariolist:
            i = i + 1
            print '*****************************************************************'
            print 'Run Scenario ' + str(i) + '   :  ' + aline
            print '*****************************************************************'
            sTempCommand = 'multimech-run ' + aline

            sSubp = subprocess.Popen(sTempCommand, shell=True, stdout=subprocess.PIPE)
            while sSubp.poll() == None:
                print sSubp.stdout.readline()
        self.endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self._collectReport()

    def _ParrallelConfig(self, sConfig,run_time = 30,rampup = 0,results_ts_interval = 1,progress_bar = 'on',console_logging = 'on',xml_report = 'off',threads = 10):
        wf = open(sConfig, 'w')
        sGlobalCfg= '[global]\r\n' \
                    'run_time = '+run_time+'\r\n' \
                    'rampup = '+rampup+'\r\n' \
                    'results_ts_interval = '+results_ts_interval+'\r\n' \
                    'progress_bar = '+progress_bar+'\r\n' \
                    'console_logging = '+console_logging+'\r\n' \
                    'xml_report = '+xml_report+'\r\n'
        wf.write(sGlobalCfg)
        i = 1
        # print self.scenariolist
        for scenariotemp in self.scenariolist:
            wf.write('[user_group - ' + str(i) + ']\r\n')
            i = i + 1
            wf.write('threads = '+threads+'\r\n')
            wf.write('script = ' + scenariotemp + 'v_user.py\r\n')
        wf.close()

    def _MergParralleScript(self,run_time,rampup,results_ts_interval,progress_bar,console_logging,xml_report,threads):

        sCurScenario = self.strCurPath + '/Parralle_Scenario/'
        if not os.path.exists(sCurScenario):
            os.makedirs(sCurScenario)
        self.scenariolist = []
        self._collectScenario()
        if len(self.scenariolist) <= 0:
            # print 'No Performance Test Scenario Under Current Test WorkSpace'
            return 0
        sCruScenarioTestScript = sCurScenario + 'test_scripts/'
        if os.path.exists(sCruScenarioTestScript):
            shutil.rmtree(sCruScenarioTestScript)
        os.makedirs(sCruScenarioTestScript)
        sConfig = sCurScenario + 'config.cfg'
        self._ParrallelConfig(sConfig,run_time,rampup,results_ts_interval,progress_bar,console_logging,xml_report,threads)
        for ascenario in self.scenariolist:

            for root, dirs, files in os.walk(self.strCurPath + '/' + ascenario + '/test_scripts/'):
                for file in files:
                    shutil.copyfile(os.path.join(self.strCurPath + '/' + ascenario + '/test_scripts/', file),
                                    sCruScenarioTestScript + file)
                    # shutil.copyfile

    def pRun(self,run_time = 30,rampup = 0,results_ts_interval = 1,progress_bar = 'on',console_logging = 'on',xml_report = 'off',threads = 10):
        self._MergParralleScript(run_time,rampup,results_ts_interval,progress_bar,console_logging,xml_report,threads)
        if len(self.scenariolist) <= 0:
            print 'No Performance Test Scenario Under Current Test WorkSpace'
            return 0
        # self.startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        sTempCommand = 'multimech-run Parralle_Scenario'
        sSubp = subprocess.Popen(sTempCommand, shell=True, stdout=subprocess.PIPE)
        print '##Performance Test is running，Please wait!!'
        while sSubp.poll() == None:
            print sSubp.stdout.readline()

        # self.endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self._mvReport()


'''
if __name__ == '__main__':
    arun = alasRun()
    arun.pRun()
    arun.sRun()
'''

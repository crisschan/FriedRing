#!/usr/bin/env python
#coding=utf-8
'''
author:Crisschan
time:2016-7-1
'''
from mitmproxy.models.http import HTTPRequest
from mitmproxy.models.http import HTTPResponse
class F2requests():
    def __init__(self,fnamescript):
        self.fscript = open(fnamescript,'w+')
        self.__InitScript()
    def __del__(self):
        self.fscript.close()
    def F2Req(self,request):
        self.request = request
        if str(self.request.method) == 'GET':
            self.__F2Get()
        else:
            self.__F2Post()
    #insert the request host information
    def __InsertHost(self):
        self.fscript.write(self.__Insert8blank()+'######'+str(self.request.host)+'#######')
    # insert the  time stamp of start
    def __InsertTimeStampStart(self):

        self.__InsertBlankRow()
        self.__InsertHost()
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'# start : ')
        self.fscript.write(str(self.request.timestamp_start))

        self.__InsertBlankRow()
    #inser the time stamp of end
    def __InsertTimeStampEnd(self):
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'# end : ')
        self.fscript.write(str(self.request.timestamp_end))

        self.__InsertBlankRow()
    #insert the global import
    def __InitScript(self):
        strPreScript = '#!/usr/bin/env python\r\n'
        strPreScript=strPreScript+'#coding=utf-8\r\n'
        strPreScript=strPreScript+'import requests\r\nimport json\r\nimport time\r\n\r\ndef script():'
        self.fscript.write(strPreScript)
        self.__InsertBlankRow()
    #insert a blank row to script
    def __InsertBlankRow(self):
        self.fscript.write('\r\n')
    #insert the assert target point
    def __InserAssert(self):
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'#insert the assert or other check point    #exp. print r.text')
        self.__InsertBlankRow()
    #insert the http header
    def __F2Header(self):
        strT = str(self.request.headers)
        strT = '\"' + strT
        strT = strT.replace('\r\n', '\n')
        strT = strT.replace('\n', '","')
        #strT = strT.replace('\n', '",\r\n"') #for format header
        strT = strT.replace(': ', '":"')
        strT = '{' + strT[:-2] + '}'
        return strT
    def __Insert8blank(self):
        return '      '
    def __F2Get(self):
        #print 'get --'
        self.__InsertTimeStampStart()
        #insert the header
        self.fscript.write(self.__Insert8blank()+'headers='+self.__F2Header())
        self.__InsertBlankRow()
        # insert the get request
        strRquest = 'http://'+str(self.request.host)+str(self.request.path)
        strRquest=self.__Insert8blank()+'r=requests.get("'+strRquest+'",headers=headers)'
        self.fscript.write(strRquest)
        self.__InsertTimeStampEnd()
        self.__InserAssert()
    def __F2Post(self):
        self.__InsertTimeStampStart()
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'headers=' + self.__F2Header())
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'payload = "'+self.request.content+'"')
        self.__InsertBlankRow()
        strRquest = 'http://'+str(self.request.host) + str(self.request.path)
        strRquest = self.__Insert8blank()+'r=requests.post("' + strRquest + '",data=payload,headers=headers)'
        self.fscript.write(strRquest)
        self.__InsertTimeStampEnd()
        self.__InserAssert()


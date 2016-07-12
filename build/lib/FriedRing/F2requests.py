#!/usr/bin/env python
#coding=utf-8
'''
author:Crisschan
time:2016-7-1

author:Crisschan
time 2016-7-11 modi for the headers check the " to \"
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

    def __InsertHost(self):
        # insert the request host information
        self.fscript.write(self.__Insert8blank()+'######'+str(self.request.host)+'#######')
        # insert the request host information
    def __InsertTimeStampStart(self):
        # insert the request host information
        self.__InsertBlankRow()
        self.__InsertHost()
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'# start : ')
        self.fscript.write(str(self.request.timestamp_start))

        self.__InsertBlankRow()

    def __InsertTimeStampEnd(self):
        # inser the time stamp of end
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'# end : ')
        self.fscript.write(str(self.request.timestamp_end))

        self.__InsertBlankRow()

    def __InitScript(self):
        # insert the global import
        strPreScript = '#!/usr/bin/env python\r\n'
        strPreScript=strPreScript+'#coding=utf-8\r\n'
        strPreScript=strPreScript+'import requests\r\nimport json\r\nimport time\r\n\r\ndef script():'
        self.fscript.write(strPreScript)
        self.__InsertBlankRow()

    def __InsertBlankRow(self):
        # insert a blank row to script
        self.fscript.write('\r\n')

    def __InserAssert(self):
        # insert the assert target point
        self.__InsertBlankRow()
        self.fscript.write(self.__Insert8blank()+'#insert the assert or other check point    #exp. print r.text')
        self.__InsertBlankRow()

    def __F2Header(self):
        # insert the http header
        # modi add the replace " to \"
        strT = str(self.request.headers)
        strT= strT.replace('\"','\\\"')
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


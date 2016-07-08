#!/usr/bin/env python
#coding=utf-8
'''
author:Crisschan
time:2016-7-8
'''
import  os
import commands
class FRun():
    def __init__(self,fscriptsolution):
        self.fscriptsolution = fscriptsolution
        self.__Run()
    def __Run(self):

         commands.getoutput('multimech-run '+self.fscriptsolution)


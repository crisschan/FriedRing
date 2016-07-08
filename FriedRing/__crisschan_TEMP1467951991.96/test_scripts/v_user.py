#!/usr/bin/env python
#coding=utf-8
import requests
import json
import time
import script
class Transaction(object):
    def __init__(self):
        #self.custom_timers={}
        pass
    def run(self):
        #start_timer = time.time()
        script.script()
        #latency = time.time() - start_timer
        #user's transaction 
        #self.custom_timers['Transaction_Custom']=latency
if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    #print trans.custom_timers
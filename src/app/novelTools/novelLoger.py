# -*- coding: utf-8 -*-
import time
class Log(object):
    def createLog(self):
        with open('log', 'w+') as f:
            f.write('log start:')

    def log(self, logContent):
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        with open('log', 'a+') as f:
            if type(logContent) == str:
                f.write('%s %s'%(t,logContent))
            elif type(logContent) == unicode:
                f.write('%s %s'%(t,logContent.encode('utf-8')))

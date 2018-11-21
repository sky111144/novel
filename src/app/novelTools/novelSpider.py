# -*- coding: utf-8 -*-
import requests
from novelLoger import Log


class novelSpider(Log):
    def __init__(self):
        Log.__init__(self)
    	self.headers = {
    		"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
    		"Referer": 'http://www.baidu.com'
    	}

    def getHtml(self, url):
        r = requests.get(url, headers = self.headers)
        r.encoding = 'utf-8'
        self.log('end -- html -- %s\n'%url)
        return r.text.encode('utf-8')

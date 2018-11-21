# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from novelLoger import Log

class novelParser(Log):
    def __init__(self):
        Log.__init__(self)

    def parseNovelData(self, novelHomeHtml, novelHomeUrl):
        soup = BeautifulSoup(novelHomeHtml, 'html.parser')
        novelInfo = {}
        try:
            info = soup.find_all(id='info')[0]
            intro = soup.find_all(id='intro')[0]
            novelInfo['novelName'] = info.h1.get_text()
            novelInfo['novelAuthor'] = info.p.get_text()[5:]
            novelInfo['novelIntro'] = intro.get_text().strip().replace('\n','')
            novelInfo['novelImg'] = 'https://www.qu.la' + soup.find_all(id='fmimg')[0].img.attrs['src']
            novelInfo['lastUpdate'] = ''
            self.log('end -- novelInfo -- %s\n'%novelInfo['novelName'])
        except Exception as e:
            novelInfo['novelName'] = ''
            novelInfo['novelAuthor'] = ''
            novelInfo['novelIntro'] = ''
            novelInfo['novelImg'] = ''
            novelInfo['lastUpdate'] = ''
            self.log('error -- novelInfo -- %s\n'%novelInfo['novelName'])
        return novelInfo

    def parseCharptList(self, novelHomeHtml, novelHomeUrl):
        soup = BeautifulSoup(novelHomeHtml, 'html.parser')
        charptList = soup.find_all('dd')
        novelData = []
        for charpt in charptList:
            if charpt.a is not None:
                charptData = {}
                a = charpt.a
                if 'book' in a.get('href'):
                    charptData['charptUrl'] = 'https://www.qu.la' + a.get('href')
                    charptData['charptName'] = a.get_text()
                    charptData['charptContent'] = ''
                    novelData.append(charptData)
                    self.log('end -- %s -- %s\n'%(novelHomeUrl, charptData['charptName']))
        return novelData

    def parseCharptContent(self, charptHtml, charptUrl):
        soup = BeautifulSoup(charptHtml, 'html.parser')
        charptContent = soup.find_all(id='content')[0].prettify()
        charptContent = re.sub(r'<.+?>|dudu[1-3]\(\);|!!.*|readx\(\);','',charptContent)
        charptContent = re.sub(r'(\n\ ){1,2}','<br/>', charptContent)
        self.log('end -- charptContent -- %s\n'%charptUrl)
        return  charptContent

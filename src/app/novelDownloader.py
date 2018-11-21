# -*- coding: utf-8 -*-
from novelTools.novelSpider import novelSpider
from novelTools.novelParser import novelParser
from novelTools.novelORM import Site, Novel, session
from sqlalchemy import func
import time

class novelDownloader(novelSpider, novelParser):
    def __init__(self):
        novelSpider.__init__(self)
        novelParser.__init__(self)
        self.siteNovelUrl = 'https://www.qu.la/book/'

    def getCharptContent(self, novelId=None, charptNum=None):
        '''
        @desc：下载某书章节内容
        @param：novelId 小说id
        @param：charptNum 章节数量
        '''
        if novelId == None and charptNum == None:
            novelId = session.query(Site).count()
            if novelId == 0 :
                return None
            charpts = session.query(Novel).filter_by(
                charptContent=''
            ).all()
        elif novelId == None and type(charptNum) == int:
            charpts = session.query(Novel).filter_by(
                charptContent=''
            ).limit(charptNum)
        elif type(novelId) == int and charptNum == None:
            charpts = session.query(Novel).filter_by(
                novelId=novelId,
                charptContent=''
            ).all()
        elif type(novelId) == int and type(charptNum) == int:
            charpts = session.query(Novel).filter_by(
                novelId=novelId,
                charptContent=''
            ).limit(charptNum)

        for charpt in charpts:
            charptHtml = self.getHtml(charpt.charptUrl)
            charptContent = self.parseCharptContent(charptHtml, charpt.charptUrl)
            session.query(Novel).filter_by(id=charpt.id).update({
                Novel.charptContent: charptContent
            })
            session.commit()
            time.sleep(1)

    def getCharptList(self, num):
        '''
        @desc：下载若干本小说章节列表、相应小说信息
        @param：num 小说数量
        '''
        curNovelNum = session.query(Site).count()
        for novelId in range(curNovelNum+1,curNovelNum+1+num):
            novelHomeUrl = self.siteNovelUrl + str(novelId)
            novelHomeHtml = self.getHtml(novelHomeUrl)
            novelInfo = self.parseNovelData(novelHomeHtml, novelHomeUrl)
            session.add(Site(
                novelName = novelInfo['novelName'],
                novelHomeUrl = novelHomeUrl,
                novelAuthor = novelInfo['novelAuthor'],
                novelIntro = novelInfo['novelIntro'],
                novelType = 'unknown',
                novelImg= novelInfo['novelImg'],
                lastUpdate= novelInfo['lastUpdate'],
                novelIsFinished = 0,
                charptIsFinished = 0
            ))
            charpts = self.parseCharptList(novelHomeHtml, novelHomeUrl)
            for charpt in charpts:
                session.add(Novel(
                    novelId = novelId,
                    charptName = charpt['charptName'],
                    charptUrl = charpt['charptUrl'],
                    charptContent = charpt['charptContent']
                ))
            session.commit()
            time.sleep(1)

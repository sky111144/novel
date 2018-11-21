#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 创建数据库
engine = create_engine("mysql+mysqldb://root:zhongguozhiwang@127.0.0.1:3306/novel?charset=utf8", max_overflow = 5)

# 生成一个SqlORM 基类
Base = declarative_base()

class Site(Base):
    '''
    @ 表结构：网站小说列表
    '''
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True)
    novelName = Column(String(100))
    novelHomeUrl = Column(String(1024))
    novelAuthor = Column(String(80))
    novelType = Column(String(30))
    novelIntro = Column(Text)
    novelImg = Column(String(1024))
    lastUpdate = Column(String(40))
    novelIsFinished = Column(Integer)
    charptIsFinished = Column(Integer)

class Novel(Base):
    '''
    @ 表结构：小说章节列表
    '''
    __tablename__ = 'novel'
    id = Column(Integer, primary_key=True)
    novelId = Column(Integer)
    charptName = Column(String(100))
    charptUrl = Column(String(1024))
    charptContent = Column(Text)


# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
Base.metadata.create_all(engine)

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = sessionmaker(bind=engine)
session = Session()

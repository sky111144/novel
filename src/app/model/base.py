#!/usr/bin/python
#coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# 创建数据库
engine = create_engine("mysql+mysqldb://root:root@127.0.0.1:3306/novel?charset=utf8", max_overflow = 5)

# 生成一个SqlORM 基类
Base = declarative_base()

class Shelf(Base):
    '''
    @ 表结构：书架信息
    '''
    __tablename__ = 'shelf'
    id = Column(Integer, primary_key=True)
    novelId = Column(Integer)
    userId = Column(Integer)

class Comment(Base):
    '''
    @ 表结构：评论信息
    '''
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    novelId = Column(Integer)
    userId = Column(Integer)
    comment = Column(String(600))
    time = Column(String(35))

class Message(Base):
    '''
    @ 表结构：站内信
    '''
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    senderId = Column(Integer)
    receiverId = Column(Integer)
    message = Column(String(2550))
    time = Column(String(100))

class User(Base):
    '''
    @ 表结构：用户基本信息
    '''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(300))
    password = Column(String(100))
    email = Column(String(100))

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

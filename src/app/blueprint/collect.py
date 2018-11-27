#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

collectBlueprint = Blueprint(
    'collect',
    __name__
)

@collectBlueprint.route('/collect/<int:novelId>', methods=['GET'])
def collectNovel(novelId):
    userId = request.cookies.get('userId')
    if userId is not None:
        userId = int(userId)
    isCollected = g.dbSession.query(Shelf).filter_by(
        novelId=novelId,
        userId=userId
    ).count()

    result = jsonify({
        'status': 'fail',
        'msg': '收藏失败'
    })
    if isCollected == 0 and userId is not None:
        g.dbSession.add(Shelf(
            novelId=novelId,
            userId=userId
        ))
        g.dbSession.commit()
        result = jsonify({
            'status': 'success',
            'msg': '收藏成功'
        })
    return result
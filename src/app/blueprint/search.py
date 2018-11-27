#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

searchBlueprint = Blueprint(
    'search',
    __name__
)
def object_to_dict(data, flag):
    if flag == 'search':
        result = []
        for novel in data:
            result.append({
                'id': novel.id,
                'name': novel.novelName,
                'author': novel.novelAuthor,
                'img': novel.novelImg,
                'intro': novel.novelIntro,
                'lastUpdate': novel.lastUpdate
            })
    return result



@searchBlueprint.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query != '':
        novel = g.dbSession.query(Site).filter(
            or_(Site.novelName.like('%%%s%%'%query))
        ).all()
        return jsonify(object_to_dict(novel, 'search'))
    else:
        return jsonify({
            'status': 'fail',
            'msg': '搜索失败',
            'data': []
        })

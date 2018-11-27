#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

def object_to_dict(data, flag):
    if flag == 'shelf':
        result = {
            'status': 'success',
            'data': []
        }
        for novel in data:
            result['data'].append({
                'id': novel.id,
                'name': novel.novelName,
                'author': novel.novelAuthor,
                'img': novel.novelImg,
                'intro': novel.novelIntro,
                'lastUpdate': novel.lastUpdate,
            })
    elif flag == 'novel':
        charpts = data['charpts']
        info = data['info']
        result = {
            'info': {
                'id': info.id,
                'name': info.novelName,
                'author': info.novelAuthor,
                'img': info.novelImg,
                'lastUpdate': info.lastUpdate.charptName,
                'type': info.novelType,
                'intro': info.novelIntro
            },
            'charpts': []
        }
        for charpt in charpts:
            result['charpts'].append({
                'id': charpt.id,
                'name': charpt.charptName
            })
    elif flag == 'charpt':
        result = {
            'id': data.id,
            'name': data.charptName,
            'content': data.charptContent
        }
    return result

homeBlueprint = Blueprint(
    'home',
    __name__
)

@homeBlueprint.route('/novel/list/<int:novelNum>')
def novelList(novelNum):
    novel = g.dbSession.query(Site).limit(novelNum)
    return jsonify(object_to_dict(novel, 'shelf'))

@homeBlueprint.route('/shelf')
def shelf():
    userId = request.cookies.get('userId')
    shelf = g.dbSession.query(Site).join(Shelf, Site.id == Shelf.novelId).filter(Shelf.userId == userId).all()
    return jsonify(object_to_dict(shelf, 'shelf'))

@homeBlueprint.route('/novel/<int:id>')
def novel(id):
    data = {}
    charpts = g.dbSession.query(Novel).filter_by(novelId=id).all()
    page = request.values.get('page')
    size = request.values.get('size')
    if page is not None and size is not None:
        page = int(request.values.get('page'))
        size = int(request.values.get('size'))
        data['charpts'] = charpts[(page-1)*size:page*size]
    else :
        data['charpts'] = charpts
    data['info'] = g.dbSession.query(Site).filter_by(id=id).first()
    data['info'].lastUpdate = charpts[-1]
    return jsonify(object_to_dict(data, 'novel'))

@homeBlueprint.route('/novel/<int:id>/<int:charptId>')
def charpt(id, charptId):
    novel = g.dbSession.query(Novel).filter_by(id=charptId, novelId=id).first()
    return jsonify(object_to_dict(novel, 'charpt'))
#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

dataBlueprint = Blueprint(
    'data',
    __name__
)

@dataBlueprint.route('/novel/count')
def novelCount():
    count = g.dbSession.query(Site).count()
    return jsonify({
        'status': 'success',
        'data': {
           'count': count
        }
    })

@dataBlueprint.route('/charpt/count')
def charptCount():
    count = g.dbSession.query(Novel).count()
    return jsonify({
        'status': 'success',
        'data': {
           'count': count
        }
    })
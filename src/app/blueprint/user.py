#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

userBlueprint = Blueprint(
    'user',
    __name__
)

@userBlueprint.route('/user/<int:userId>', methods=['GET'])
def userInfo(userId):
    userInfo = g.dbSession.query(User).filter_by(id=userId).first()
    return jsonify({
        'status': 'success',
        'msg': '获取用户信息成功',
        'data': {
            'username': userInfo.username,
            'id': userInfo.id
        }
    })

@userBlueprint.route('/register', methods=['POST'])
def register():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    email = request.get_json().get('email')
    result = jsonify({ 
        'status': 'fail', 
        'msg': '注册失败'
    })
    if username == None or password == None or email == None:
        return result

    user = g.dbSession.query(User).filter_by(email=email).all()
    isExsisted = len(user) == 0
    if isExsisted:
        g.dbSession.add(User(
            username=username,
            password=password,
            email=email
        ))
        result = jsonify({
            'status': 'success',
            'msg': '注册成功',
            'data': {
                'username': username
            }
        })
        flaskSession['username'] = username
        g.dbSession.commit()
    res = make_response(result)
    return res


@userBlueprint.route('/login', methods=['POST'])
def login():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    user = g.dbSession.query(User).filter_by(username=username,password=password).all()
    isIllegal = len(user) == 1
    result = {
        'status': 'fail',
        'msg': '登录失败'
    }
    if isIllegal:
        flaskSession['username'] = username
        result = {
            'status': 'success',
            'msg': '登录成功',
            'data': {
                'userId': user[0].id,
                'username': username
            }
        }
    res = make_response(jsonify(result))
    if isIllegal:
        res.set_cookie('isLogin', 'true', expires=g.expires)
        res.set_cookie('username', username, expires=g.expires)
        res.set_cookie('userId', str(user[0].id), expires=g.expires)
    return res

@userBlueprint.route('/logout', methods=['POST'])
def logout():
    if 'username' in flaskSession:
        flaskSession['username'] = None
    res = make_response(jsonify({
        'status': 'success',
        'msg': '退出成功'
    }))
    res.set_cookie('username', '')
    res.set_cookie('userId', '')
    return res

@userBlueprint.route('/changePassword', methods=['POST'])
def changePassword():
    oldPassword = request.get_json().get('oldPassword')
    newPassword = request.get_json().get('newPassword')
    username = request.get_json().get('username')
    isUserself = g.dbSession.query(User).filter_by(username=username,password=oldPassword).count()
    result = {
        'status': 'fail',
        'msg': '修改失败'
    }
    if isUserself == 1:
        g.dbSession.query(User).filter_by(username=username).update({
            User.password: newPassword
        })
        g.dbSession.commit()
        result = {
            'status': 'success',
            'msg': '修改成功'
        }
    return jsonify(result)

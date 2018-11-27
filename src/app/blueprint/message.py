#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

def object_to_dict(data, flag):
    if flag == 'message':
        result = {
            'status': 'success',
            'data': []
        }
        for message in data:
            result['data'].append({
                'senderId': message[0].senderId,
                'receiverId': message[1].id,
                'receiverName': message[1].username,
                'message': message[0].message,
                'time': message[0].time
            })
    elif flag == 'userMessage':
        result = {
            'status': 'success',
            'data': []
        }
        for message in data:
            result['data'].append({
                'userId': message[1].id,
                'username': message[1].username,
                'message': message[0].message,
                'time': message[0].time
            })
    return result
    


messageBlueprint = Blueprint(
    'message',
    __name__
)

# 查询用户个人私信
@messageBlueprint.route('/user/message', methods=['GET'])
def userMessage():
    userId = request.cookies.get('userId')
    messages = g.dbSession.query(Message,User).join(User, Message.receiverId==User.id).filter(
        Message.senderId==userId
    ).all()
    return jsonify(object_to_dict(messages,'userMessage'))

@messageBlueprint.route('/message/<int:userId>', methods=['POST', 'GET'])
def message(userId):
    senderId = request.cookies.get('userId')
    if request.method == 'POST':
        message = request.get_json().get('message')
        g.dbSession.add(Message(
            senderId=senderId,
            receiverId=userId,
            message=message,
            time=g.time
        ))
        g.dbSession.commit()
        return jsonify({
            'status': 'success',
            'msg': '私信成功'
        })
    elif request.method == 'GET':
        messages = g.dbSession.query(Message,User).join(User, User.id==Message.receiverId).filter(
            Message.senderId==senderId,
            Message.receiverId==userId
        ).all()
        return jsonify(object_to_dict(messages,'message'))

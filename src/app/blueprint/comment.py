#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message

def object_to_dict(data, flag):
    if flag == 'comment':
        result = {
            'status': 'success',
            'data': []
        }
        for comment in data:
            result['data'].append({
                'userId': comment[1].id,
                'username': comment[1].username,
                'novelId': comment[0].novelId,
                'comment': comment[0].comment,
                'time': comment[0].time
            })
    elif flag == 'userComment':
        result = {
            'status': 'success',
            'data': []
        }
        for comment in data:
            result['data'].append({
                'novelId': comment[1].id,
                'novelName': comment[1].novelName,
                'comment': comment[0].comment,
                'time': comment[0].time
            })
    return result


commentBlueprint = Blueprint(
    'comment',
    __name__
)

# 查询用户个人评论
@commentBlueprint.route('/user/comment', methods=['GET'])
def userComment():
    userId = request.cookies.get('userId')
    comments = g.dbSession.query(Comment,Site).join(Site, Comment.novelId==Site.id).filter(
        Comment.userId==userId
    ).all()
    return jsonify(object_to_dict(comments,'userComment'))


@commentBlueprint.route('/comment/<int:novelId>', methods=['POST', 'GET'])
def comment(novelId):
    userId = request.cookies.get('userId')
    if request.method == 'POST':
        comment = request.get_json().get('comment')
        g.dbSession.add(Comment(
            userId=userId,
            novelId=novelId,
            comment=comment,
            time=g.time
        ))
        g.dbSession.commit()
        return jsonify({
            'status': 'success',
            'msg': '评论成功'
        })
    elif request.method == 'GET':
        comments = g.dbSession.query(Comment,User).join(User, User.id==Comment.userId).filter(
            Comment.novelId==novelId
        ).all()
        return jsonify(object_to_dict(comments,'comment'))

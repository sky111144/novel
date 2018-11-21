#!/usr/bin/python
#coding=utf-8
from flask import Blueprint,render_template,make_response,redirect,request,g,jsonify
from flask import session as flaskSession
from sqlalchemy import distinct,desc,or_
from app.model.base import User,Site,Novel,Shelf,Comment,Message
from novelSpider.task import createDownloader

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
    elif flag == 'search':
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
    elif flag == 'comment':
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
    elif flag == 'message':
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

@homeBlueprint.route('/search', methods=['GET'])
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

@homeBlueprint.route('/user/<int:userId>', methods=['GET'])
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

# 查询用户个人评论
@homeBlueprint.route('/user/comment', methods=['GET'])
def userComment():
    userId = request.cookies.get('userId')
    comments = g.dbSession.query(Comment,Site).join(Site, Comment.novelId==Site.id).filter(
        Comment.userId==userId
    ).all()
    return jsonify(object_to_dict(comments,'userComment'))

# 查询用户个人私信
@homeBlueprint.route('/user/message', methods=['GET'])
def userMessage():
    userId = request.cookies.get('userId')
    messages = g.dbSession.query(Message,User).join(User, Message.receiverId==User.id).filter(
        Message.senderId==userId
    ).all()
    return jsonify(object_to_dict(messages,'userMessage'))

@homeBlueprint.route('/message/<int:userId>', methods=['POST', 'GET'])
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

@homeBlueprint.route('/comment/<int:novelId>', methods=['POST', 'GET'])
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

@homeBlueprint.route('/collect/<int:novelId>', methods=['GET'])
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

@homeBlueprint.route('/register', methods=['POST'])
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

@homeBlueprint.route('/login', methods=['POST'])
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

@homeBlueprint.route('/logout', methods=['POST'])
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

@homeBlueprint.route('/changePassword', methods=['POST'])
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

@homeBlueprint.route('/novel/count')
def novelCount():
    count = g.dbSession.query(Site).count()
    return jsonify({
        'status': 'success',
        'data': {
           'count': count
        }
    })

@homeBlueprint.route('/charpt/count')
def charptCount():
    count = g.dbSession.query(Novel).count()
    return jsonify({
        'status': 'success',
        'data': {
           'count': count
        }
    })

@homeBlueprint.route('/task/getCharptList', methods=['GET'])
def getCharptList():
    downloader = createDownloader()
    downloader.getCharptList(1)
    return jsonify({
        'status': 'success'
    })

@homeBlueprint.route('/task/getCharptContent', methods=['GET'])
def getCharptContent():
    downloader = createDownloader()
    downloader.getCharptContent(charptNum=1)
    return jsonify({
        'status': 'success'
    })

#!/usr/bin/python
#coding=utf-8
import time
from logging import FileHandler,WARNING,DEBUG
from random import random
from os import urandom
from math import ceil

from flask import Flask,request,render_template,jsonify,redirect,url_for,make_response,g,send_from_directory
from flask import session as flaskSession
from flask_cors import CORS
from sqlalchemy import distinct,desc

from blueprint.home import homeBlueprint
from model.base import Session

def create_app():
    app = Flask(__name__)
    app.secret_key = '\x14:\xe3\x1aB\xc5|\x10iQ\xd9 \xdf\xce\x19\x83\xd3\xb7s\x97\xee(T\xb8\xb25\xd3\xd1\xe1NJ\x92'
    CORS(app, supports_credentials=True, origins=['http://localhost:8080','http://localhost:3000','http://www.novelyouwant.com','https://www.novelyouwant.com','https://sky111144.github.com'])

    # 日志记录
    fileHandler = FileHandler('app/log/warning.log')
    fileHandler.setLevel(WARNING)
    app.logger.addHandler(fileHandler)

    # 注册蓝图
    app.register_blueprint(homeBlueprint)

    @app.before_request
    def before_request():
        g.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        g.expires = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+86400))
        g.dbSession = Session()
        path = request.path
        if ('/logout' in path or '/changePassword' in path or '/user' in path) and ('username' not in flaskSession and request.cookies.get('username') != flaskSession['username']):
            return jsonify({
                'status': 'fail',
                'msg': '请先登录'
            })

    @app.teardown_request
    def teardown_request(exception):
        g.dbSession.close()

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    @app.route('/novel/list/<int:novelNum>')
    def novelList(novelNum):
        return redirect(url_for('home.novelList'))

    @app.route('/shelf')
    def shelf():
        return redirect(url_for('home.shelf'))

    @app.route('/search')
    def search():
        return redirect(url_for('home.search'))

    @app.route('/novel/<int:id>')
    def novel(id):
        return redirect(url_for('home.novel'))

    @app.route('/novel/<int:id>/<int:charptId>')
    def charpt(id, charptId):
        return redirect(url_for('home.charpt'))

    @app.route('/comment/<int:novelId>')
    def comment(novelId):
        return redirect(url_for('home.comment'))

    @app.route('/message/<int:userId>')
    def message(userId):
        return redirect(url_for('home.message'))

    @app.route('/user/<int:userId>')
    def userInfo(userId):
        return redirect(url_for('home.userInfo'))

    @app.route('/user/comment/<int:userId>')
    def userComment(userId):
        return redirect(url_for('home.userComment'))

    @app.route('/user/message/<int:userId>')
    def userMessage(userId):
        return redirect(url_for('home.userMessage'))

    @app.route('/novel/count')
    def novelCount():
        return redirect(url_for('home.novelCount'))

    @app.route('/charpt/count')
    def charptCount():
        return redirect(url_for('home.charptCount'))

    @app.route('/collect/<int:novelId>')
    def collectNovel(novelId):
        return redirect(url_for('home.collectNovel'))

    @app.route('/register')
    def register():
        return redirect(url_for('home.register'))

    @app.route('/login')
    def login():
        return redirect(url_for('home.login'))

    @app.route('/logout')
    def logout():
        return redirect(url_for('home.logout'))

    @app.route('/changePassword')
    def changePassword():
        return redirect(url_for('home.changePassword'))

    @app.route('/task/getCharptList')
    def getCharptList():
        return redirect(url_for('home.getCharptList'))

    @app.route('/task/getCharptContent')
    def getCharptContent():
        return redirect(url_for('home.getCharptContent'))

    return app

# coding=utf-8
from flask import Flask, current_app
from flask_cors import CORS
from redis import StrictRedis
import os

from main.get.login.login import login
from main.get.info.info import info
from main.get.info.info2 import info2
from main.send.info.table import table

# 设置SECRET_KEY为随机数
app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
appContent = app.app_context()
appContent.push()
# 将SECRET_KEY存入Redis数据库
redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
redis.set('SECRET_KEY', current_app.config['SECRET_KEY'])
appContent.pop()

# 跨域请求设置
CORS(app, resources=r'/*')

app.register_blueprint(login, url_prefix='/get')
app.register_blueprint(info, url_prefix='/get')
app.register_blueprint(info2, url_prefix='/get')
app.register_blueprint(table, url_prefix='/send')

if __name__ == '__main__':
    app.run(host='172.27.0.13', port=5009, debug=True)
    # app.run()

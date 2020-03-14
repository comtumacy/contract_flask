# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import json
from main.get.login.login_sql import login_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
login = Blueprint("login", __name__)


@login.route('/login', methods=['POST', 'GET'])
def login_fun():
    data = request.json

    response = make_response()
    response.content_type = 'application/json'
    status = login_sql(data['username'], data['password'])
    if status == 1:
        # 获取SECRET_KEY
        redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
        secret_key = redis.get('SECRET_KEY')
        expiration = 3600
        s = Serializer(secret_key, expires_in=expiration)  # expiration是过期时间
        token = s.dumps({'username': data['username']})
        token = str(token, 'utf-8')
        redis.set(data['username'], token)
        redis.expire(data['username'], 3600)
        post_data = {'info': '登录成功', 'token': token, 'username': data['username']}
        response = make_response(json.dumps(post_data))
        response.content_type = 'application/json'
        response.status_code = 200
        return response
    elif status == 0:
        post_data = {'info': '密码错误'}
        response = make_response(json.dumps(post_data))
        response.content_type = 'application/json'
        response.status_code = 401
        return response
    else:
        post_data = {"info": "此用户不存在"}
        response = make_response(json.dumps(post_data))
        response.content_type = 'application/json'
        response.status_code = 403
    return response

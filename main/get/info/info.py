# coding=utf-8
from flask import Blueprint, make_response, request
from redis import StrictRedis
import json
from main.get.info.info_sql import info_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
info = Blueprint("info", __name__)


@info.route('/info', methods=['POST', 'GET'])
def info_fun():
    data = request.json
    token = data['token']
    username = data['username']

    redis = StrictRedis(host='localhost', port=6379, db=0, password='Liyitong97!')
    token_get = redis.get(username)
    token_get = str(token_get)
    token_get = token_get.replace("b'", "")
    token_get = token_get.replace("'", "")

    if token != token_get:
        post_data = {'info': '登录失效，请重新登录'}
        response = make_response(json.dumps(post_data))
        response.content_type = 'application/json'
        response.status_code = 401
        return response
    else:
        response = make_response()
        response.content_type = 'application/json'
        all_list, title, title2 = info_sql()
        post_data = {"content": all_list, "title1": title, "title2": title2}
        response = make_response(json.dumps(post_data))
        response.content_type = 'application/json'
        response.status_code = 200
        return response

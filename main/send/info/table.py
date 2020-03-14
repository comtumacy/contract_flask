# coding=utf-8
from flask import Blueprint, make_response, request
import json
from main.send.info.table_sql import table_sql

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
table = Blueprint("table", __name__)


@table.route('/table', methods=['POST', 'GET'])
def table_fun():
    data = request.json
    field = data['field']
    content = data['content']
    response = make_response()
    response.content_type = 'application/json'
    content_list = []
    for key in content:
        content_list.append(content[key])
    table_sql(field, content_list)
    post_data = {"info": '提交成功'}
    response = make_response(json.dumps(post_data))
    response.content_type = 'application/json'
    response.status_code = 200
    return response

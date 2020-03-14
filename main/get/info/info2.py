# coding=utf-8
from flask import Blueprint, make_response
import json
from main.get.info.info_sql2 import info_sql2

# 创建一个蓝图的对象，蓝图就是一个小模块的概念
info2 = Blueprint("info2", __name__)


@info2.route('/info2', methods=['POST', 'GET'])
def info2_fun():
    response = make_response()
    response.content_type = 'application/json'
    result_list2, all_list2 = info_sql2()
    post_data = {"content2": all_list2, "list2": result_list2}
    response = make_response(json.dumps(post_data))
    response.content_type = 'application/json'
    response.status_code = 200
    return response

# coding=utf-8
import pymysql


def login_sql(username, password):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='contract',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select password FROM user WHERE username = '{}';".format(username)
    cursor.execute(sql1)
    conn.commit()
    tup = cursor.fetchall()
    if len(tup) == 0:
        status = -1
    elif tup[0][0] == password:
        status = 1
    else:
        status = 0
    cursor.close()
    conn.close()
    return status


# coding=utf-8
import pymysql


def info_sql2():
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='contract',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * FROM colname"
    sql2 = "SHOW full COLUMNS FROM colname"
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()
    cursor.execute(sql2)
    conn.commit()
    result2 = cursor.fetchall()
    all_list = []
    result2list = []
    for item in result2:
        result2list.append(item[0])
    for i in range(len(result1)):
        tup_list = list(result1[i])
        all_dict = dict(zip(result2list, tup_list))
        all_list.append(all_dict)
    cursor.close()
    conn.close()
    return result2list, all_list



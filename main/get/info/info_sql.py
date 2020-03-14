# coding=utf-8
import pymysql


def info_sql():
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='contract',
                           charset='utf8')
    cursor = conn.cursor()
    sql1 = "select * FROM info"
    sql2 = "SHOW full COLUMNS FROM info"
    sql3 = "select * FROM colname"
    sql4 = "SHOW full COLUMNS FROM colname"
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()
    cursor.execute(sql2)
    conn.commit()
    result2 = cursor.fetchall()
    cursor.execute(sql3)
    conn.commit()
    result3 = cursor.fetchall()
    cursor.execute(sql4)
    conn.commit()
    result4 = cursor.fetchall()
    all_list = []
    all_list2 = []
    result2list = []
    result4list = []
    for item in result2:
        result2list.append(item[0])
    for i in range(len(result1)):
        tup_list = list(result1[i])
        all_dict = dict(zip(result2list, tup_list))
        all_list.append(all_dict)
    for item in result4:
        result4list.append(item[0])
    for i in range(len(result3)):
        tup_list = list(result3[i])
        all_dict = dict(zip(result4list, tup_list))
        all_list2.append(all_dict)
    cursor.close()
    conn.close()
    title = []
    title2 = []
    for i in range(len(all_list2)):
        title.append(all_list2[i]['colname'])
        title2.append(all_list2[i]['colnamech'])
    return all_list, title, title2

info_sql()


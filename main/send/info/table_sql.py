# coding=utf-8
import pymysql


def table_sql(table_title, table_content):
    conn = pymysql.connect(host='139.155.33.105', port=2707, user='root', password='Liyitong97!', db='contract',
                           charset='utf8')
    cursor = conn.cursor()
    field = ''
    content = ''
    for i in range(len(table_title)):
        if i == 0:
            field = table_title[i]
            content = table_content[i]
        else:
            field = field + ',' + table_title[i]
            content = content + "','" + table_content[i]
    sql1 = "INSERT into info ({}) VALUES ('{}')".format(field, content)
    cursor.execute(sql1)
    conn.commit()
    result1 = cursor.fetchall()
    cursor.close()
    conn.close()


# table_sql()


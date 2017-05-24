# -*- coding:utf-8 -*-
import MySQLdb
conn = MySQLdb.connect(host="localhost",user="rootttt",passwd="",db="test",charset="utf8")
cursor = conn.cursor()


def select(sql, key):
    sql = sql
    key = key
    param = (key,)
    cursor.execute(sql, param)
    conn.commit()
    n = cursor.fetchall()
    for data in n:
        return data
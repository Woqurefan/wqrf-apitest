# -*- coding:utf-8 -*-
import time
import hashlib
#文件功能:自定义某些urL ,比如需要URL鉴权的,
#各个加密算法:
def md5(obj):
    'MD5加密,默认为小写32位'
    m2 = hashlib.md5()
    m2.update(obj)
    return m2.hexdigest()
def sha1(obj):
    'sha1加密'
    s1= hashlib.sha1()
    s1.update(obj)
    return s1.hexdigest()
#--------------------------------------------用户配置部分:根据需要的参数来组装成URL
# test_host = 'http://192.168.2.252:8081'
test_host = 'http://＊＊＊＊'
online_host = 'https://＊＊＊＊＊＊＊'

#left
host = test_host
#--------------------------------------------
def nomal(url):
    '正常拼接host,无任何修改,可一键配置是否切换到线上HOST'
    return host+url

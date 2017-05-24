# -*- coding:utf-8 -*-
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
from selenium import webdriver
import time
import gettoken
import unittest,re
from HTMLTestRunner import HTMLTestRunner
import urllib2,urllib
import json,time,requests

#获取推送的结果,类型,时间。 被Text.yanzheng来调用
def de_token(type,value):  #获取device_token
    typee = ''
    if type == 1 :
        typee = 'mobile'
    elif type == 2:
        typee = 'email'
    url = ""+str(value)+"&searchType="+typee
    headers = {'Content-Type': 'application/json',
               'Authorization': ''}
    response = requests.request("GET", url, headers=headers)
    print
    try:
        if  json.loads(response.text)['data'][0]['subject']['last_push_token'] != None :
            return json.loads(response.text)['data'][0]['subject']['last_push_token']
        elif json.loads(response.text)['data'][1]['subject']['last_push_token'] != None:
            return json.loads(response.text)['data'][1]['subject']['last_push_token']
    except:
        print u'没有token'
        return 0
def chatuisong(type,value) :  #查最新的推送
    token = de_token(type,value)
    url = ""
    body = {'query': {'device_token':token}, 'cursor': {'skip': 0, 'limit': 1}}
    pa = json.dumps(body)
    req = urllib2.Request(url, pa)
    req.add_header('Content-Type','application/json')
    req.add_header('Authorization','')
    response = urllib2.urlopen(req)
    s= json.loads(response.read())
    # 是否成功,推送类型,推送内容
    times = str(s['data'][0]['create_time'])
    print s['data'][0]['status'],s['data'][0]['event'],str(int(times[11:13])+8)+times[14:16]
    return [s['data'][0]['status'],s['data'][0]['event'],str(int(times[11:13])+8)+times[14:16]]
def yanzheng(self, type, value):
    time.sleep(3)
    timex = time.ctime()
    timex = timex[11:13] + timex[14:16]
    time.sleep(2)
    shiji = chatuisong(type, value)
    timey = shiji[2]
    if abs(int(timey) - int(timex)) < 2:
        print 'right---------'
        return [shiji[0], shiji[1]]
    else:
        print 'wrong---------'
        return []
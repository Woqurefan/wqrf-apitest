# -*- coding:utf-8 -*-

# 文件描述:获取TOKEN/KEY的模块

import time
import urllib
import urllib2
import json
import requests
from api_test_WQRF.req import req as reqno   #sin_req没有log,eve_req有log
from api_test_WQRF.api_doc.make import *

#------------------------------------------------------------用户配置部分:获取TOKEN接口,需要调用上面的POST_DEMO
def token_e(email,pas='qwerty'):
    data = login_email([email,pas])
    back = json.loads(reqno(data)['res_body'])
    try:
        return back['access_token']
    except:
        return 'havenottoken,pleas check user!'

def token_p(num,pas='qwerty',country='86'):
    data = login_mobile([country,num,pas])
    back = json.loads(reqno(data)['res_body'])
    try:
        return back['access_token']
    except:
        return 'havenottoken,pleas check user!'
#------------------------------------------------------------

def token_duoxi(account,uuid):
    data = login_duoxi([account,uuid])
    back = json.loads(reqno(data)['res_body'])
    try:
        return back['data']['authToken']
    except:
        return 'havenottoken,pleas check user!'
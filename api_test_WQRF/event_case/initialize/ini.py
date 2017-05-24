# -*- coding:utf-8 -*-
#文件功能:初始化用户实体
# -*- coding:utf-8 -*-
#文件功能:接收账户,删除账号下的所有好友
import time,sys,os
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
import unittest,re
from random import randint
from HTMLTestRunner import HTMLTestRunner
from api_test_WQRF.req import req as reqno  #sin_req没有log,eve_req有log
from api_test_WQRF.api_doc.make import *
from api_test_WQRF.token_get import *
def clear_friend(user_token):
    '清除账号下的好友'
    # 获取所有好友的UUID
    data = friend_new_getList()
    back = json.loads(reqno(data,user_token)['res_body'])
    list = back['locators']
    for i in list:
        #进行删除操作
        data = friend_new_delete([i["uuid"]])
        back = json.loads(reqno(data, user_token)['res_body'])
        assert back['ret'] == 0

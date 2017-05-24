# -*- coding:utf-8 -*-
#文件功能:事件流测试用例
import time,sys,os
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
import unittest,re
from random import randint
from api_test_WQRF.WQRFhtmlRunner import HTMLTestRunner
from api_test_WQRF.req_log import *
from api_test_WQRF.api_doc.make import *
from api_test_WQRF.token_get import *
from api_test_WQRF.event_case.initialize import ini
from api_test_WQRF.event_case.assert_response import deep_assert
from api_test_WQRF.Email import Send_Mail
#--------------------------------------------用户配置部分:业务流用例,data=url+body,t=token
#------------------------------实际返回:SJ 预期返回:YQ,所有BODY必须要封装到一个列表中,req方法如果需要传入token则要写好,需要加入head则继续加
#------------------------注意:self.assertEqual()失败的话,后面的语句会不执行
#-------------------注意,要传入的参数放在一个列表里!
#---------------需要传入token的话,请req(data,token)
#-------------提BUG时注意不要启动最后的 删除之类的用例脚本

all = []
token = token_e('tecom')
for i in range(40):
    #鉴权
    print u'鉴权',i
    data1 = nut_auth(["116.412636","39.946162","37","281471487111771"])
    back1 = json.loads(req(data1,token)['res_body'])
    all.append(back1['ret'])
    if back1['ret'] == 303:
        break
    #绑定
    # time.sleep(0.5)
    print u'绑定',i
    data2 = nut_bind_text()
    back2 = json.loads(req(data2,token)['res_body'])
    # time.sleep(1)
    #解绑
    print u'删除',i
    data3 = nut_delete(["0bc5dfd3-90f8e61bb075"])
    back3 = json.loads(req(data3,token)['res_body'])
    # time.sleep(2)
print all
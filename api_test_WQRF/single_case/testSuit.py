# -*- coding:utf-8 -*-
#文件功能:单接口自身的通用测试用例套件,主要可以自定义每个接口都经常要测试的功能:分为:成功,鉴权失败,参数为空,URL错误
#会自动分析数据并组装成各个用例。但是显示起来 一个接口 只算一条用例。后续会改

import unittest,re
from HTMLTestRunner import HTMLTestRunner
import urllib2,urllib
import json,time
from api_test_WQRF.req import *
import copy,sys
reload(sys)
sys.setdefaultencoding('utf8')

def Suit_new(name,data,token):
    if data!='':   #判断是否有数据body
        rr = name(data)
    else:
        rr =name()  #无body则不传
    mode = rr[0]   #分解重组后的body
    url = rr[1]
    try:
        body =rr[2]
    except:
        body = {}
    token = token
    res ={}  #返回总值
    # 1.完全正确的跑通用例
    ss = req(rr, token,**{'User-agent':'asdasdsd'})
    res.setdefault(u'01_正确用例* ' +str(rr) + ' *:', (ss['time_des'], ss['res_body']))
    # 2.URL错误的用例,后面+'aaa'
    try:
        ss = req((mode, url + 'aaa', body), token,**{'User-agent':'asdasdsd'})
        res.setdefault(u'02_u r l错误* {' + str(url + 'aaa') + '} *:', (ss['time_des'], ss['res_body']))
    except urllib2.HTTPError ,e:
        res.setdefault(u'02_u r l错误* {' + str(url + 'aaa') + '} *:', (u'URL错误: ☆ ☆ ☆ ☆ ☆ ',str(e)))
    # 3.token错误的用例,为'aaa'  无token的此条用例不执行
    if token != '':
        ss = req(rr, 'aaa',**{'User-agent':'asdasdsd'})
        res.setdefault(u'03_token错误* {' + str(head_demo + ':"aaa"') + '}*:', (ss['time_des'], ss['res_body']))
    else:
        res.setdefault(u'03_token错误* {' + str(head_demo + ':"aaa"') + '}*:',(u' 无token',u'-所以不执行此用例'))
    #-------------------------------------------------------------------
    # 4.body各个参数为指定值的算法
    data_old = copy.deepcopy(data)
    def every(can):
        data_new = data
        for I in range(len(data_new)):                #根据所传参数计划循环次数
            null_data = u'url组成'
            data_new[I]=can                          #清空参数
            r = name(data_new)                      #求出哪个参数是空的算法,最多显示2级参数名
            for i in range(len(r[2])):
                if r[2].values()[i] == can :
                    null_data = r[2].keys()[i]
                    break
                elif  type(r[2].values()[i]) == dict:
                    for j in range(len(r[2].values()[i])):
                        if r[2].values()[i].values()[j] == can:
                            null_data = r[2].keys()[i]+'/'+r[2].values()[i].keys()[j]
                            break                       #可继续升级代码,添加第三层判断
                else:
                    pass
            ss = req(r,token,**{'User-agent':'asdasdsd'})                       #发送请求
            res.setdefault(u'%s_%s参数为%s类型:%s * ' % (str(I + 4).zfill(2),null_data,str(type(can))[7:-2],repr(can)) + str(data_new) + ' *:', (ss['time_des'], ss['res_body']))
            data_new=copy.deepcopy(data_old)        #深拷贝还原对象

    ############################################## 用户可自定义部分
    ready = [9,'b',None,r"s' or '1'='1",r's" or "1"="1']#设置好要测试的参数,每个接口的每个参数都会遍历这个列表
    ##############################################
    for i in ready:
        every(i)
    return res






# -*- coding:utf-8 -*-
from __future__ import division
# 文件功能:封装了请求发送
import urllib2,urllib
import json,time,requests
import edit
timeoutt = edit.timout
requests.packages.urllib3.disable_warnings()
head_demo = edit.head_demo
try:
    pro = edit.daili
    print u'开启代理',edit.daili
except:
    pro = {}
#------返回OBJECT : res中目前包含 时间 和 返回值
def req(data,t='',**hea):
    def post_demo(url,body,token):
        global res
        url = url
        headers = dict({'Content-Type': 'application/json', head_demo: t}.items()+hea.items())
        pa = json.dumps(body)
        try:
            req = requests.post(url, pa, headers=headers,timeout=timeoutt,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des':inout,'res_body':s}
    def get_demo(url,token):
        global res
        url = url
        headers = dict({'Content-Type': 'application/json', head_demo: t}.items()+hea.items())
        try:
            req = requests.get(url,headers=headers,timeout=timeoutt,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des': inout, 'res_body': s}
    def put_demo(url,body,token):
        global res
        url = url
        pa = json.dumps(body)
        headers = dict({'Content-Type': 'application/json', head_demo: t}.items()+hea.items())
        try:
            req = requests.put(url,pa,headers=headers,timeout=timeoutt,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des': inout, 'res_body': s}
    def delete_demo(url,token):
        global res
        url = url
        headers = dict({'Content-Type': 'application/json', head_demo: t}.items()+hea.items())
        try:
            req = requests.delete(url, headers=headers,timeout=timeoutt,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des': inout, 'res_body': s}
    def post_f_demo(url,file_groupp=(),body={''},token=''):
        '带文件'
        global res
        url = url
        headers =dict({ head_demo: t}.items()+hea.items())
        files = {file_groupp[0]: open(file_groupp[1], 'rb')}  #这里写好file的key名
        datat = body
        try:
            req = requests.post(url, files=files, data=datat, headers=headers,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des': inout, 'res_body': s}
    def put_f_demo(url,file_groupp=(),body={''},token=''):
        '带文件'
        global res
        url = url
        headers = dict({ head_demo: t}.items()+hea.items())
        files = {file_groupp[0]: open(file_groupp[1], 'rb')}
        datat = body
        try:
            req = requests.put(url, files=files, data=datat, headers=headers,proxies=pro,verify=False)
            sec = req.elapsed.microseconds
            s = req.text
            inout = 'time:' + str(sec / 1000000) + u's ☆ ☆ ☆ ☆ ☆'
        except requests.exceptions.ReadTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        except requests.exceptions.ConnectTimeout, e:
            inout = 'time out!!!!!'
            s = str(e)
        res = {'time_des': inout, 'res_body': s}

    if data[0] == 'post':
        post_demo(data[1],data[2],t)
    elif data[0] == 'get':
        get_demo(data[1],t)
    elif data[0] == 'put':
        put_demo(data[1],data[2],t)
    elif data[0] == 'delete':
        delete_demo(data[1],t)
    elif data[0] == 'post_f':
        post_f_demo(data[1],data[2],data[3],t)
    elif data[0] == 'put_f':
        put_f_demo(data[1], data[2],data[3],t)
    else:
        print u'接口的请求方式错误!请检查api_doc/make.py下的:',data[1],u'的mode!'
        exit(0)
    return res

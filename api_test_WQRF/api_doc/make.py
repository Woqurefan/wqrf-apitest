# -*- coding:utf-8 -*-
#文件功能:接口文档
import url_make as ur
import json,time
#--------------------------------------------用户配置部分:添加接口文档,仅能设置mode,url,body,url需要正常返回
# 如果参数是从其他接口返回值中获取的,最好强制类型转换。如str(id),注意:行参必须为一个元组,哪怕只有一个参数也要加逗号
# GET,DELETE方式请求,没有BODY最好也写,也要返回BODY,body={}即可;如把URL当参数传的时候,拼接时必须全部转换成str
# multipart/form-data 格式的请把MODE写成 post_f 或 put_f, 要写好file_group(文件的key,文件绝对路径)
# 注意,所有接口函数,在调用时要把参数传的数量写够,即使没有,也要用''补全
# 请求参数一样时,需要用二维列表或 列表套元组
# 发送表单请求时,DATA(body)必须不能JSON.dumps() ,不然会报错。但是可以在BODY里把深层的值单独进行JSON.DUMPS()
#-----------------------------------

def GetCurrentRelease((vcode,os)):
    '获取最新版本'
    mode = 'get'
    url="/＊＊＊＊＊/?versionCode=%s&os=%s"%(str(vcode),str(os))
    body = {}
    return [mode,ur.nomal(url),body]
def DownloadApp((id,)):
    '＊＊＊＊'
    mode = 'get'
    url = "/＊＊＊＊/%s"%(str(id))
    body = {}
    return [mode, ur.nomal(url), body]


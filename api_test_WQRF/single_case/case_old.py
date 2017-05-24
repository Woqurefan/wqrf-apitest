# -*- coding:utf-8 -*-
#文件功能:单接口自身的测试用例
import time
import sys,os
import unittest,re,json
import xlrd,xlwt,xlutils
from xlutils.copy import copy
from HTMLTestRunner import HTMLTestRunner
from api_test_WQRF import req
from api_test_WQRF.api_doc.make import *
from api_test_WQRF.token_get import *
import api_test_WQRF.single_case.testSuit as suit
reload(sys)
sys.setdefaultencoding('utf8')


#--------------------------------用户配置部分:可选用unittest框架生成用例,或调用直接显示所有返回值的Test_new类
#无body的请用''来占位,注意多个接口尽量不要用同样的实体,以免TOKEN混乱导致用例结果异常,也可以设定TOKEN全局变量,可以提高速度
#在此写入要测试的接口函数名称和参数值⬇️⬇️⬇️ 注意token或data/body没有的情况下要用''单引号占位!!!,注意列表结构,注意接口函数名不要加括号!!!
baojing=200  #设置报警的返回值  #############################################################################################

# token_x = token_e('nt.com')  #设置全局变量token
token_x = token_duoxi('159092','991fc43064a')  #设置全局变量token

api_new=[

[GetCurrentRelease,['17','android'],token_x],
[GetCurrentRelease,['18','android'],token_x],
[GetCurrentRelease,['20','android'],token_x],
[GetCurrentRelease,['55','ios'],token_x],
[GetCurrentRelease,['100','ios'],token_x],
[GetCurrentRelease,['200','ios'],token_x],

]


class Test_new():
    def __init__(self,name,data,token):
        SZ = xlrd.open_workbook(fname,formatting_info=True)
        sz = SZ.sheet_by_index(0)
        ww = copy(SZ)
        get = suit.Suit_new(name,data,token)  # 此处有TOKEN的需要传TOKEN
        get = sorted(get.iteritems(), key=lambda d: d[0])  # 按照KEY第一位来排序
        print u'\n-----------------------------------<< 接口名:', name.__doc__,u' >>----<< 接口方法:',name.func_name, ' ' * (
        14 - len(name.func_name)), u'>>----------------------------------------------------'
        #设置字体 颜色等
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 2# May be: 8 through 63. 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray,
        style = xlwt.XFStyle()
        style.pattern = pattern
        try:
            ww.get_sheet(0).write(sz.nrows, 0,(name.__doc__).decode('utf-8'))
        except AttributeError:
            ww.get_sheet(0).write(sz.nrows, 0, (name.__doc__))
            print u'-请补全接口方法的说明!'
        ww.get_sheet(0).write(sz.nrows+1, 0,name.func_name)
        for i in range(len(get)):
            print  u'第 %s 条用例: ' %str(i + 1).zfill(2) + get[i][0] + get[i][1][0] +get[i][1][1]
            #结果写入到表中
            ww.get_sheet(0).write(sz.nrows+i,1,u'ApiTest-%s:' %str(i + 1).zfill(2))
            ww.get_sheet(0).write(sz.nrows+i,2, get[i][0])
            ww.get_sheet(0).write(sz.nrows+i,3,get[i][1][0])
            retun_data = get[i][1][1].decode('utf-8')
            if len(retun_data) < 32765:
                try:
                    if json.loads(get[i][1][1])['code'] ==baojing: #设置标红的返回值
                        ww.get_sheet(0).write(sz.nrows + i, 4, retun_data,style)
                    else:
                        ww.get_sheet(0).write(sz.nrows+i,4,retun_data)
                except:
                    ww.get_sheet(0).write(sz.nrows + i, 4,retun_data)
            else:
                ww.get_sheet(0).write(sz.nrows + i, 4, u'内容过长,无法保存')
        ww.get_sheet(0).write(sz.nrows + len(get), 0, u'~'*150)  #不同接口之间的分隔符
        os.remove(fname)
        try:
            ww.save(fname)
        except Exception,e:
            print u'文件保存出错!!!',e
if __name__ == '__main__':
    #清空表
    fname = u'/Users/zijiawang/nut-qa-doc/nutapp/api_test_WQRF/Report/suit_test.xls'
    QQ=xlrd.open_workbook(u'/Users/zijiawang/nut-qa-doc/nutapp/api_test_WQRF/Report/蓝本.xls',formatting_info=True)
    qq =QQ.sheet_by_index(0)
    WW=copy(QQ)
    try:
        os.remove(fname)
    except:
        pass
    WW.save(fname)
    test_new = Test_new
    print u'接口通用针对参数格式的测试用例执行开始...'
    tim1 = time.time()
    for i in api_new:
        try:
            test_new(name=i[0],data=i[1],token=i[2])
        except IndexError:
            print u'请补全',i[0].func_name,u'在api_new列表中的函数名,BODY,TOKEN三项'
    tim = str(time.time()-tim1).split('.')[0]
    print u'一共耗用了%s秒'%tim







#----------------------------------------------------------------------------------------------------------------------------------
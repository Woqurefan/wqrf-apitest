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
from api_test_WQRF.api_doc.ErrorCode import error_code
from api_test_WQRF.event_case.assert_response import deep_assert
from api_test_WQRF.Email import Send_Mail
import inspect,pickle
import xlrd,xlutils,xlwt
from xlutils.copy import copy
#--------------------------------------------用户配置部分:业务流用例,data=url+body,t=token
#------------------------------实际返回:SJ 预期返回:YQ,所有BODY必须要封装到一个列表中,req方法如果需要传入token则要写好,如需要加入HEAD则继续写!!
#------------------------注意:self.assertEqual()失败的话,后面的语句会不执行
#-------------------注意,要传入的参数放在一个列表里!
#---------------需要传入token的话,请req(data,token)
#---------记得全局化要复用的返回值参数
#------可配置是否要保存实际返回作为下次的预期

fp = open('switch.txt')
switch = fp.read()
fp.close()

#----------------------test_new的预期输出保存在此
xname = r'./event_case/test_new/test_new.xls'
if switch == 'w':
    # ------------------保存结果的话,会删除掉之前的所有结果。
    print u'\n即将保存实际返回结果至',xname
    w = xlwt.Workbook()
    w.add_sheet('APItest')
    w.save(xname)
def readORwrite(selfs,back):
    '读还是写,这是一个选择'
    class_name = str(selfs.__class__.__name__)
    lie = ord(class_name) - 64  # 根据其类的名称A,B来放倒表中的列里。便于查看,但是类名变了则会报错
    test_name = str(inspect.stack()[1][3])
    #----------------------
    if switch == 'r':
        SZ = xlrd.open_workbook(xname)
        sz = SZ.sheet_by_index(0)
        if len(str(back)) > 32766 :  #如果字符串过长的,需要去俩个单元格获取!!!!
            try:
                print u'超长情况-深层判断出现的问题:'
                PA1 =  sz.cell_value(int(test_name[-2:]) - 1, lie-1)
                PA2 = sz.cell_value(int(test_name[-2:]) - 1, 255-lie)
                yq = eval(PA1+PA2)  # -2 代表最高支持1-99的序号用例
                deep_assert(back, yq)
            except Exception, e:
                print class_name, u'超长情况-提取预期失败: ', e
        else:
            try:
                print u'深层判断出现的问题:'
                yq = eval(sz.cell_value(int(test_name[-2:])-1 ,lie))  #-2 代表最高支持1-99的序号用例
                deep_assert(back,yq)
            except Exception,e:
                print class_name,u'提取预期失败: ',e
        #------------------提取结果的前提是一定要有预期
    elif switch == 'w':
        #-----------------------
        time.sleep(0.3)
        SZ = xlrd.open_workbook(xname)
        ww = copy(SZ)
        if len(str(back)) > 32766 :  #如果字符串过长的,需要进行拆分!!!!
            try:
                ww.get_sheet(0).write(int(test_name[-2:]) - 1, lie-1, str(back)[:20000])
                ww.get_sheet(0).write(int(test_name[-2:]) - 1, 255-lie, str(back)[20000:])
                os.remove(xname)
                ww.save(xname)
                print u'超长情况--保存实际返回 至 预期 成功!'
            except Exception, e:
                print class_name, u'超长情况--保存预期失败: ', e
        else: #字符串长度为超长
            try:
                ww.get_sheet(0).write(int(test_name[-2:])-1,lie,str(back))
                os.remove(xname)
                ww.save(xname)
                print u'保存实际返回 至 预期 成功!'
            except Exception,e:
                print class_name,u' 保存预期失败: ',e

    else:
        print u'配置文件出错 请检查switch.txt'

class A(unittest.TestCase):
    u'流程:好友功能'
    @classmethod
    def setUpClass(cls):  # 用户需要手动设置,进行判断是否初始化成功。可自选在前或后,def setUpClass(cls) 或 def tearDownClass(cls):
        u'初始化所有实体'
        cls.token_1 = token_e('fri3d@1.com')  #设置全类变量token,可以大大节省运行时间,并有利于反馈BUG
        cls.token_2 = token_e('fr3ie1.com')
        try:  # 初始化函数
            ini.clear_friend(cls.token_1)
            print '\n'+cls.__doc__+u' - - - - 初始化成功...'
        except:
            print '\n'+cls.__doc__+u' - - - - 无需初始化或失败...'
    def test_01(self):
        u'添加邮箱好友'
        data = friend_new_addE(['friend@11.com'])  # 输入要测试的数据,data=(mode,url,body),
        back = json.loads(req(data,self.token_1)['res_body'])  # 获取实际返回值,需要传入token的话,请req(data,token)
        YQ = 0  # 输入预期的值
        SJ = back['ret']  # 设置实际返回,如果需要传入TOKEN等header,请务必填写!
        self.assertEqual(SJ, YQ, error_code(SJ, YQ))
   

class B(unittest.TestCase):
    u'流程:安全区域功能'
    @classmethod
    def setUpClass(cls):  # 用户需要手动设置,进行判断是否初始化成功。可自选在前或后,def setUpClass(cls) 或 def tearDownClass(cls):
        u'初始化所有实体'
        cls.token_1 = token_e('wqran1.com')  # 设置全类变量token,可以大大节省运行时间,并有利于反馈BUG
        cls.token_2 = token_e('wqrf@n2.com')
        try:  # 初始化函数
            ini.clear_safe(cls.token_1)
            print '\n\n' + cls.__doc__ + u' - - - - 初始化成功...'
        except:
            print '\n\n' + cls.__doc__ + u' - - - - 无需初始化或失败...'
    def test_01(self):
        u'添加安全区域'
        data = safe_add(['sa1',39,116])  # 输入要测试的数据,data=(mode,url,body),
        back = json.loads(req(data, self.token_1)['res_body'])  # 获取实际返回值,需要传入token的话,请req(data,token)
        YQ = 0  # 输入预期的值
        SJ = back['ret']  # 设置实际返回,如果需要传入TOKEN等header,请务必填写!
        self.assertEqual(SJ, YQ,error_code(SJ,YQ))
        readORwrite(self, back)
    




















#---------------------------------------------------------------------------------------
def make_suit(suit_list):
    suit = unittest.makeSuite(suit_list[0])
    for i in range(1, len(suit_list)):
        suit.addTest(unittest.makeSuite(suit_list[i]))
    return suit
if __name__ =="__main__":
    # #######################用户配置行
    allsuit=[A,B]
    suit_list =allsuit  # 设置要启动的流程用例类名
    make_suit(suit_list)
    # ##################################
    try:
        filename = u'/'.join(os.getcwd().split('/')[:-2]) + u'/Report/业务逻辑接口测试报告_new.html'
        fp = file(filename, 'wb')
    except:
        filename = u'./Report/业务逻辑接口测试报告_new.html'  # 从主界面启动
        fp = file(filename, 'wb')
    runner = HTMLTestRunner(fp, title=u'测试服新接口测试', description=u'用例执行报告',fname=filename.split('/')[-1])
    runner.run(make_suit(suit_list))
    fp.close()
    Send_Mail(filename)
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

class A(unittest.TestCase):
    u'流程1:流程'
    NecessaryParameter = '' #类变量,可接收某用例的返回值中的某参数作为之后用例的传入参数
    @classmethod
    def setUpClass(cls):  # 用户需要手动设置,进行判断是否初始化成功。可自选在前或后,def setUpClass(cls) 或 def tearDownClass(cls):
        u'初始化所有实体'
        cls.token_1 = 'xxxxx'  #设置类变量,使用self.token_1
        try:  # 初始化函数
            print '\n\n'+cls.__doc__+u' - - - - 初始化成功...'
        except:
            print '\n\n'+cls.__doc__+u' - - - - 无需初始化或失败...'
    def test_01(self):
        u'描述'

        data =  login_email(['wans.com','qwsty'])  #输入要测试的数据,data=(mode,url,body),
        back = json.loads(req(data,'token',**{'User-agent':'12s2412asd'})['res_body'])      #获取实际返回值,增加TOEKN,HEADER,req(data,token,countny='CN',sss='TTT')
        YQ = 0                                          #输入预期的值
        SJ = back['ret']   #设置实际返回,如果需要传入TOKEN等header,请务必填写!
        # 进行判断
        self.assertEqual(SJ,YQ)
        #深层判断,先写实际再写预期,可以提出预期,然后进行列表类的内容传入判断具体是哪个参数的问题,NULL要全部换成NONE.
        deep_assert(back,{'预期返回值':'值'})





#---------------------------------------------------------------------------------------
def make_suit(suit_list):
    suit = unittest.makeSuite(suit_list[0])
    for i in range(1, len(suit_list)):
        suit.addTest(unittest.makeSuite(suit_list[i]))
    return suit
if __name__ == '__main__':
    filename = u'/'.join(os.getcwd().split('/')[:-2])+u'/Report/业务逻辑接口测试报告_.html'
    # #######################用户配置行
    suit_list = [A]  # 设置要启动的流程用例类名
    # ##################################
    make_suit(suit_list)
    fp = file(filename, 'wb')
    runner = HTMLTestRunner(fp, title=u'接口测试', description=u'用例执行报告',fname=filename.split('/')[-1])
    runner.run(make_suit(suit_list))
    fp.close()
    Send_Mail(filename)
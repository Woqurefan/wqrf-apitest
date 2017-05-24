# -*- coding:utf-8 -*-
from __future__ import division
import time,sys,os
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
import wx.grid
import threading
import os
import wx
from random import randint

class NUTAPI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'WQRF接口测试启动界面',
                          size=(340, 260), pos=(500, 200))
        clour = ["TURQUOISE","SEA GREEN","LIGHT STEEL BLUE","MEDIUM ORCHID","BLUE VIOLET","LIGHT BLUE","GOLD","THISTLE","WHEAT"]
        cl = randint(0,len(clour)-1)
        self.SetBackgroundColour(colour=clour[cl])
        self.panel1 = wx.Panel(self, -1)
        self.SetMaxSize((340, 260))
        self.SetMinSize((340, 260))
        self.font1 = wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.fonts = wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD)
        #-----------------------
        sampleList = [u'测试服new', u'测试服old', u'测私服gps', u'正式服所有']
        self.which = wx.RadioBox(self.panel1, -1, u"请选择脚本", (20, 10), wx.DefaultSize, sampleList,3,
                                   wx.RA_SPECIFY_COLS)
        self.profile = {
                0:{'py':'./event_case/test_new/case_1.py','html':u'./Report/业务逻辑接口测试报告_new.html','xls':'./event_case/test_new/test_new.xls'},
                   1:{'py':'./event_case/test_old/case_1.py','html':u'./Report/业务逻辑接口测试报告_old.html','xls':'./event_case/test_old/test_old.xls'},
                   2:{'py':'./event_case/test_gps/cases_gps.py','html':u'./Report/业务逻辑接口测试报告_GPS.html','xls':'./event_case/test_gps/test_gps.xls'},
                   3:{'py':'./event_case/test_online/case_online.py','html':u'./Report/业务逻辑接口测试报告_online.html','xls':'./event_case/test_online/test_online.xls'}
                   }
        #------------------------

        self.bt_be = wx.Button(self.panel1, -1, label=u"启动测试", pos=(30, 100), size=(100, 21))
        self.bt_be.SetBackgroundColour("PURPLE")
        self.bt_be.SetFont(self.font1)
        self.bt_be.Bind(wx.EVT_BUTTON, self._nobc)

        self.bt_ck = wx.Button(self.panel1, -1, u"查看测试报告", pos=(30, 130),size=(100,21))
        self.bt_ck.SetBackgroundColour("PURPLE")
        self.bt_ck.SetFont(self.font1)
        self.bt_ck.Bind(wx.EVT_BUTTON, self._ck)

        self.bt_bc = wx.Button(self.panel1, -1, u"保存结果为预期", pos=(209, 100),size=(100,21))
        self.bt_bc.SetBackgroundColour("FOREST GREEN")
        self.bt_bc.SetFont(self.fonts)
        self.bt_bc.Bind(wx.EVT_BUTTON, self._bc)

        self.bt_bc = wx.Button(self.panel1, -1, u"打开预期表格", pos=(209, 130), size=(100, 21))
        self.bt_bc.SetBackgroundColour("FOREST GREEN")
        self.bt_bc.SetFont(self.fonts)
        self.bt_bc.Bind(wx.EVT_BUTTON, self._dk)

        self.bt_host = wx.Button(self.panel1, -1, u"切换\nhost", pos=(135, 98), size=(70, 55))
        self.bt_host.SetFont(self.font1)
        self.bt_host.Bind(wx.EVT_BUTTON, self._host)

        self.bt_dan = wx.Button(self.panel1, -1, u"执行\n单接口测试用例", pos=(30, 160), size=(135, 45))
        self.bt_dan.SetFont(self.font1)
        self.bt_dan.Bind(wx.EVT_BUTTON, self._dan)

        self.bt_dan_c = wx.Button(self.panel1, -1, u"查看\n单接口测试报告", pos=(175, 160), size=(135, 45))
        self.bt_dan_c.SetFont(self.font1)
        self.bt_dan_c.Bind(wx.EVT_BUTTON, self._dan_c)

        #状态显示框
        from api_test_WQRF.api_doc.url_make import host as now_host
        self.host_text = wx.StaticText(self.panel1, -1, now_host, pos=(78, 75)) #状态说明
        self.zhuangtai = wx.StaticText(self.panel1, -1,'', pos=(139, 210))

#---------------------------------------------------------

    def _host(self,event):
        fname = './api_doc/url_make.py'
        fp = open(fname,'r')
        lines = fp.readlines()
        fp.close()
        # 19行为固定的HOST对应行在url_make.py中
        if lines[19].find("host = test_host") == 0:
            lines[19] = "host = online_host\n"
            self.host_text.SetLabelText('https://*******.com')

        elif lines[19].find("host = online_host") == 0:
            lines[19] = "host = test_host\n"
            self.host_text.SetLabelText('https://*******com')
        fn = open(fname,'w')
        fn.writelines(lines)
        fn.close()

    def _nobc(self,event):
        fp = open('switch.txt', 'w')
        fp.write('r')
        fp.close()
        self._be()

    def _be(self):
        self.zhuangtai.SetLabelText(u'正在运行...')
        t = threading.Thread(target=self._yx)
        t.setDaemon(True)
        t.start()
    def _yx(self):
        file =  str(self.profile[self.which.GetSelection()]['py'])
        os.system('python '+file)
        self.zhuangtai.SetLabelText(u' 已完成...')
    def _ck(self, event):
        try:
            file =  str(self.profile[self.which.GetSelection()]['html'])
            os.system('open '+file)
        except Exception,e:
            print u'打开出错:',e

    def _dan(self,event):
        self.zhuangtai.SetLabelText(u'正在运行...')
        t = threading.Thread(target=self._dan_beg)
        t.setDaemon(True)
        t.start()

    def _dan_beg(self):
        file = './single_case/case_old.py'
        os.system('python ' + file)
        self.zhuangtai.SetLabelText(u' 已完成...')

    def _bc(self,event):
        fp = open('switch.txt','w')
        fp.write('w')
        fp.close()
        self._be()

    def _dk(self,event):
        try:
            file = str(self.profile[self.which.GetSelection()]['xls'])
            os.system('open ' + file)
        except Exception, e:
            print u'打开出错:', e

    def _dan_c(self, event):
        try:
            file = './Report/suit_test.xls'
            os.system('open ' + file)
        except Exception, e:
            print u'打开出错:', e


if __name__ == "__main__":
    app = wx.App()
    NUTAPI().Show()
    app.MainLoop()


# -*- coding:utf-8 -*-

import smtplib,time
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import datetime


# 定义发送邮件的函数
def Send_Mail(filename):
    msg = MIMEMultipart('related')
    sendfile = open(filename,'rb').read()
    att = MIMEText(sendfile,'base64','utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="WQRF_API_TestReport.html"'
    content = str('报告在附件中!')  # 正文内容
    body = MIMEText(content, 'plain', 'utf-8')  # 设置字符编码
    msg.attach(body)
    msg.attach(att)
    msgto = ['.com']  # 收件人地址 多个联系人，格式['.com', '.com']
    msgfrom = '.com'  # 寄信人地址 ,
    # msg['Cc']='lnu.com' #抄送人地址 多个地址不起作用
    msg['subject'] = 'WQRF接口框架给您发的接口测试报告'  # 主题
    msg['From'] = '.com'  # 必填否则会报554
    msg['To'] = msgto[0]
    msg['date'] = time.ctime()  # 时间
    mailuser = 'ma.co'  # 用户名
    mailpwd = 'w1990'  # 密码
    try:
        smtp = smtplib.SMTP()
        smtp.connect(r's.com')  # smtp设置
        smtp.login(mailuser, mailpwd)  # 登录
        # smtp.sendmail(msgfrom, msgto, msg.as_string())  # 发送
        smtp.close()
        print u"邮件已成功发送"
    except Exception, e:
        print e, u"邮件未成功发送"
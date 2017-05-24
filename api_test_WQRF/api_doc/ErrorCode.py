# -*- coding:utf-8 -*-
#文件功能:复制过来所有错误码。接收错误码,返回错误翻译值
#注意,错误码前后不要有空格
#注意,要补充好返回结果成功的解释,比如ret:0

code = """0 ....... 此请求不应该成功
200 WRONG_PASSWORD 密码错误
"""


code =  code.split('\n')  #给错误码进行分行处理
every = []
for i in code:
    every.append(i.split(' '))

def error_code(SJ,YQ):
    for i in range(len(every)):
        if every[i][0] == str(SJ):
            try:
                return str(SJ)+u' 不等于预期的 '+str(YQ)+u' -->>>错误原因:'+str(every[i][2])
            except:
                return str(SJ)+u' 不等于预期的 '+str(YQ)+u' -->>>错误原因:'+u'未找到该错误码对应解释!'


# -*- coding:utf-8 -*-

# yq 是预期参数,sj是实际参数
def deep_assert(sj,yq,msg=u'【接口返回值'):
    '深层判断,并输出发生错误的参数的位置路径'
    # 原则上来说,实际和预期 返回值要完全一样,但是实际上,实际返回值可以多参数,但不能少参数。所以就判断所有预期的参数是否可以在实际返回中找到,并且其值正确无误
    global mmsg,num
    mmsg = msg
    for i in yq.items():
        if i[0] in sj.keys():
            y = i[1]
            s = sj[i[0]]
            if y!=s:
                mmsg += '➝' + str(i[0])
                if type(y) == dict and type(s) == dict:
                    deep_assert(s,y,mmsg)
                else:
                    if type(s)==unicode or type(y)==unicode:
                        s=str(s)
                        y=str(y)
                    if type(y) == type(s):
                        print u'▇▇▇▇▇仅内容不同参数在[预期输出]中的绝对路径:', mmsg,u"】⇒⇒⇒ 预期:",y,u" ≠ 实际:",s
                    elif type(y)==str and type(s)==unicode:
                        print u'▇▇▇▇▇仅内容不同参数在[预期输出]中的绝对路径:', mmsg, u"】⇒⇒⇒ 预期:", y, u" ≠ 实际:", s
                    else:
                        print u'✘✘✘✘✘✘✘类型错误的参数在[预期输出]中的绝对路径:', mmsg, u"】⇒⇒⇒ 预期:",str(type(y))[7:-2]+':', y, u" ≠ 实际:",str(type(s))[7:-2]+':',s
                    mmsg = u'【接口返回值'
            else:
                pass
        else:
            print u'✘✘✘✘✘✘✘未在接口的[实际返回]中找到的参数:',msg,'➝',i[0],u'】'
            mmsg = u'【接口返回值'

# deep_assert({'a':[{'b':1},{'bb':1}]},{'a':[{'b':2},{'bb':2}]})
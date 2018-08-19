# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description: 现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.
"""

def amount_print(n):
    dict0 = {0:u'零', 1:u'壹', 2:u'贰', 3:u'叁', 4:u'肆', 5:u'伍', 6:u'陆', 7:u'柒', 8:u'捌', 9:u'玖'}
    list0 = [u'仟', u'佰', u'拾', u'万', u'仟', u'佰', u'拾', ""]
    sum_str = ""
    l = len(str(abs(n)))
    s = 10 ** (l - 1)
    i = 8 - l
    if n <0:
        sum_str += u'负'
        n = abs(n)
    if n == 0:
        sum_str += u'零'
    else:
        while s != 0:
            nu = n // s
            sum_str += dict0[nu]
            sum_str += list0[i]
            n %= s
            if n == 0:
                break
            if l - len(str(abs(n))) >= 2:
                sum_str += u'零'
            l = len(str(abs(n)))
            s = 10 ** (l - 1)
            i = 8 - l
    sum_str += u'圆'
    return sum_str

a = -500563
print(amount_print(a))
# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description: 给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数
"""

L=[2,8,3,50]
def has2(x):
    s=0
    while x%2 == 0:
        x=x/2
        s+=1
    return s

def has5(x):
    s=0
    while x%5 ==0:
        x=x/5
        s+=1
    return s

print(min(sum(map(has2,L)),sum(map(has5,L))))
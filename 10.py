# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description:给你两个正整数a和b， 输出它们的最小公倍数。
"""
a=8
b=4

#就是变相的求最大公约数
def gcd(n1,n2):
    if(n1%n2==0):
        return n2
    return gcd(n2,n1%n2)
print((a*b)/gcd(a,b))
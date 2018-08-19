# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description:给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
"""
a='acbca'
n=3

flg="NO"
for i in range(0,len(a)-n+1):
    if a[i:i+n]==a[i:i+n][::-1]:
        flg="YES"

print(flg)
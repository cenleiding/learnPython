# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description:给你两个正整数a和b， 输出它们的最大公约数。
"""

a = 3
b = 5
#常规方法
def s(a, b):
    c = min(a, b)
    while True:
        if a % c == 0 and b % c == 0:
            return c
        else:
            c -= 1

print(s(a, b))

#while转载相除
if a < b:
    a, b = b, a
while a % b:
    a, b = b, a % b
print(b)

#递归转载相除
def gongyue(a, b):
    a, b = b, a % b
    if b == 0:
        return a
    else:
        return gongyue(a, b)

print(gongyue(a, b))

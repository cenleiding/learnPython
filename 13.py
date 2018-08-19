# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description: 给你一个整数a，数出a在二进制表示下1的个数，并输出。
"""
a=7
##常规方法

max=1
while max<a:
    max=max*2

count=0
while a>0:
    if a>=max:
        a=a-max
        count+=1
    max=max//2

print(count)

#模拟手工求2进制
a=7
counter = 0
while a > 0:
    counter += a % 2
    a //= 2
print(counter)

#&逐位判断
a=7
count=0;
while(a):
    a&=(a-1);
    count+=1;
print(count);

#bin()无脑解决
print(bin(a).count("1"))
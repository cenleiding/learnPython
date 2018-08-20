# coding:utf-8

"""
@author : CLD
@time:2018/8/2021:50
@description:给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
"""

from functools import reduce
from datetime import datetime

st="00:00:01"
et="00:01:10"


#灵活使用map/reduce
L = map(lambda x, y: x - y, map(int, et.split(':')), map(int, st.split(':')))
print (reduce(lambda x, y: 60 * x + y, L))

#时间转换 !!!!!垃圾Windows，用时间戳时不能超过1970~2038,Linux 就不会
s=datetime.strptime('1999:1:1 '+st, '%Y:%m:%d %H:%M:%S').timestamp()-datetime.strptime('1999:1:1 '+et, '%Y:%m:%d %H:%M:%S').timestamp()
print(abs(int(s)))

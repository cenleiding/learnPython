# encoding:utf-8

"""
@author:CLD
@file: .py
@time:2018/8/19
@description:输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。
"""
#常规方法
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(" ".join([str(i) for i in range(2, 101) if isPrime(i)]))

#一行
print(' '.join([str(i) for i in range(2,100)if 0 not in [i%j for j in range(2,i)]]))

#素数构造器。。
def _odd():
    n = 1
    while True:
        n += 2
        yield n


def fil(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd()
    while True:
        n = next(it)
        yield n
        it = filter(fil(n), it)


for n in primes():
    if n < 100:
        print(n,end=' ')
    else:
        break
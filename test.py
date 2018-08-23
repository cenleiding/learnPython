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

s=0
for i in range(1,n//2):
    if i in primes() and (n-i) in primes():
        s+=1
print(s)
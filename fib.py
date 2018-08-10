def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b    #同时进行      #等于t=(b,a+b)
        n = n + 1                         #a=t[0]
    return 'done'                         #b=t[1]

print(fib(6))

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b                #将函数变为generator,每次next()遇到yield停止
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib2(6)
for n in f:
	print(n)

while True:
    try:
        x = next(f)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

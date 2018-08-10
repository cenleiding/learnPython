def yang(max):
	n,a=0,[1,1]
	while n<max:
		print(a)
		a=[0]+a+[0]
		b=[]
		for i,value in enumerate(a):
			b.append(a[int(i)])
		print(b)
yang(2)

def f(x):
    return x * x

print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
		


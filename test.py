L=[2,-3,3,50]

p=[0]*len(L)
p[0]=L[0]
for i in range(1,len(L)):
	p[i]=max(L[i]+p[i-1],L[i])
print(max(p))



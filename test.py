w=[1,2]
n=[2,1]
s=[0]
a=[0]
for i,ele in enumerate(n):
    for j in range(ele+1):
        a.append(j*w[i])
    s=[x+y for x in s for y in a]
    a=[0]




print(len(set(s)))
n=2
m=1
wang= [[0 for col in range(n+2)] for row in range(m+2)]
mi=100000
def yima(x,y,n,m,b):
    global mi
    global wang
    if x<0 or x>n or y<0 or y>m:
        return
    if x==n and y==m:
        wang[x][y]=1
        if b<mi:
            mi=b
        return
    if wang[x][y]==1:
        return
    wang[x][y]=1
    yima(x+2,y+1,n,m,b+1)
    yima(x+2,y-1,n,m,b+1)
    yima(x-2,y+1,n,m,b+1)
    yima(x-2,y-1,n,m,b+1)
    yima(x + 1, y + 2, n, m, b + 1)
    yima(x + 1, y - 2, n, m, b + 1)
    yima(x - 1, y + 2, n, m, b + 1)
    yima(x - 1, y - 2, n, m, b + 1)

yima(0,0,n,m,0)
if mi==100000:
    print("-1")
else:
    print(mi)

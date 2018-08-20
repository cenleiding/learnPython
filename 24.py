# coding:utf-8

"""
@author : CLD
@time:2018/8/2023:21
@description:下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
"""

#丑丑的深度优先
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
if wang[n][m]==1:
    print(mi)
else:
    print("-1")
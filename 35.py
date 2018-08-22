# coding:utf-8

"""
@author : CLD
@time:2018/8/2223:00
@description:
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).
"""
#动态规划
L=[2,-3,3,50]

p=[0]*len(L)
p[0]=L[0]
for i in range(1,len(L)):
	p[i]=max(L[i]+p[i-1],L[i])
print(max(p))
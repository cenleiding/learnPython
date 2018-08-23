# coding:utf-8

"""
@author : CLD
@time:2018/8/2322:44
@description:
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个非连续子序列，使其和最大，输出最大子序列的和。
这里非连续子序列的定义是，子序列中任意相邻的两个数在原序列里都不相邻。
例如，对于L=[2,-3,3,50]， 输出52（分析：很明显，该列表最大非连续子序列为[2,50]).
"""

#动态规划状态转移
L=[2,-3,3,50]
max_1=0 #选自己
max_2=0 #不选自己
for i in range(len(L)):
    max_1,max_2=max_2+L[i],max(max_1,max_2)
print(max(max_1,max_2))


#更简约，因为不选自己的情况已经包含在前面的值中了
for i in range(2,len(L)):
    L[i]=L[i]+max(max(L[0:i-1]),0)
print(max(L))
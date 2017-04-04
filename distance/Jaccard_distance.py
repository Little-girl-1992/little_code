# -*-coding:utf-8-*-

"""样本A与样本B是两个n维向量，而且所有维度的取值都是0或1。
例如：A(0111)和B(1011)。
我们将样本看成是一个集合，
1表示集合包含该元素，0表示集合不包含该元素。
P：样本A与B都是1的维度的个数

q：样本A是1，样本B是0的维度的个数

r：样本A是0，样本B是1的维度的个数

s：样本A与B都是0的维度的个数
"""

from numpy import *
import scipy.spatial.distance as dist  # 导入scipy距离公式

matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

print "dist.jaccard:", dist.pdist(matV,'jaccard')

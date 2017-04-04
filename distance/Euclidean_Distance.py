# -*-coding:utf-8-*-

"""欧式距离公式"""

from numpy import *

def example():
	va=mat([1,2,3])
	# 向量A
	vb=mat([1,2,3])
	# 向量B 
	dist=sqrt((va-vb)*((va-vb).T))
	# 欧式距离公式
	print dist
example()
# 欧氏距离：
#Euclidean_distance
from math import sqrt

def Euclidean_distance(vector1,vector2):
    length = len(vector1)

    TSum = sum([pow((vector1[i] - vector2[i]),2) for i in range(len(vector1))])

    SSum = sqrt(TSum)

    return SSum

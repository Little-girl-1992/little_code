# -*-coding:utf-8-*-

"""几何中夹角余弦可用来衡量两个向量方向的差异，
机器学习中借用这一概念来衡量样本向量之间的差异"""

from numpy import *
# 两个向量A,B 
vector1=[0.2,0.3,0.5]
vector2=[0.1,0.2,0.3]
# 余弦夹角
cosV12= dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))

print cosV12

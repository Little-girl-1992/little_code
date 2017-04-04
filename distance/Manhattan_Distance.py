# -*-coding:utf-8-*-

"""曼哈顿距离
从名字就可以猜出这种距离的计算方法了。
想象你在曼哈顿要从一个十字路口开车到另外一个十字路口，
驾驶距离是两点间的直线距离吗？
显然不是，除非你能穿越大楼。
实际驾驶距离就是这个“曼哈顿距离”(L1范数)。
而这也是曼哈顿距离名称的来源，
曼哈顿距离也称为城市街区距离
"""

from numpy import *

va=mat([1,2,3])
# 向量A
vb=mat([3,4,5])
# 向量B 
dist=sum(abs(va-vb))
#曼哈顿距离
print dist

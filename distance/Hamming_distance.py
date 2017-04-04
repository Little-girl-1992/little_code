# -*-coding:utf-8-*-

"""两个等长字符串s1与s2之间的汉明距离
定义为将其中一个变为另外一个所需要作的最小替换次数。"""

from numpy import *
matV= mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

smstr = nonzero(matV[0]-matV[1]);

print shape(smstr[0])[1]

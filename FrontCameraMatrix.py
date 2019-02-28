#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 14:43
# @Author  : Dongyang
# @Site    : 
# @File    : FrontCameraMatrix.py
# @Software: PyCharm Community Edition

from numpy import *
import pandas as pd

camera = mat([[4220.888,3256.42,1],[1228.651,3238.1,1],[1241.748,1098.876,1]])#abc
camera_I = camera.T.I
robot = mat([[1625.29,-1020.04,1],[1637.05,862.67,1],[2977.26,849.11,1]])
tranMatrix = robot.T.dot(camera_I)#直接变换


camera_R = mat([[1090.588,3080.093,1],[1126.529,172.425,1],[3212.43,198.2087,1]])
camera_R_I = camera_R.T.I
robot_R = mat([[841.15,1573.56,1],[-1029.57,1556.50,1],[-1044.51,2901.59,1]])
tranMatrix_R = robot_R.T.dot(camera_R_I)#直接变换


print("前方变换矩阵：\n",tranMatrix)
print("右侧变换矩阵：\n",tranMatrix_R)
dfF = pd.DataFrame(tranMatrix)
dfR = pd.DataFrame(tranMatrix_R)
dfF.to_csv("FrontCameraMatriaxTest",sep=',')
dfR.to_csv("RightCameraMatriaxTest",sep=',')
#F

camera_test = mat([[4233.985,1117.196,1],[2731.318,2177.648,1]])#d,o点
camera_Real = mat([[2965.18,-1021.02,1]])#Robot坐标（自创）

#R
camera_R_test = mat([[3176.489,3105.877,1],[2151.509,1639.151,1]])
robot_R_real = mat([825.80,2918.36,1])

robot_result = tranMatrix.dot(camera_test.T)

robot_R_result = tranMatrix_R.dot(camera_R_test.T)



print("="*20)
print("="*20)
print("第四点在Robot中实际坐标：\n",camera_Real.T)
print("="*20)
print("前方第四点计算坐标：\n",robot_result)
print("="*20)
print("右侧第四点在Robot中实际坐标：\n",robot_R_real.T)
print("="*20)
print("右侧第四点计算坐标：\n",robot_R_result)
print("="*20)

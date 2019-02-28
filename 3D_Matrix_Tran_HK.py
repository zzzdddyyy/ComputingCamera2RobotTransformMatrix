#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 14:42
# @Author  : Dongyang
# @Site    : 
# @File    : 3D_Matrix_Tran_HK.py
# @Software: PyCharm Community Edition

from numpy import *
import pandas as pd
#import numpy as np


chessBoard = mat([[150,0,0],[150,150,0],[330,300,0]])

p_ = mat([2255.3,-206.8,339.5])

#print(p_.T)

chess_ = mat([[0,0,0.0000001,1],[150,0,0.000001,1],[150,150,0.000001,1],[330,300,0.000001,1]])

RobotWorld = mat([[2255.3,-206.8,339.5,1],[2256.89,-56.75,338.74,1],[2407.12,-58.54,339.11,1],[2559.62,119.96,339.93,1]])

#M_Extr = mat([[-0.999,-0.098,-0.052,131.7089],[0.0098,-1,0.004,269.2923],[-0.0052,0.003,1,3071.5],[0,0,0,1]])
#print(RobotWorld)
#print(chess_.T.I)

#print(RobotWorld.T)
tranMatrix_B2W = RobotWorld.T.dot(chess_.T.I)
#print(tranMatrix)

inMatrix = mat([[4972.23150568487,0,2725.15982031644],[0,4971.45915125274,1819.36358395942],[0,0,1]])

exMatrix = mat([[-0.999,-0.0098,-0.0052,131.7089],[0.0098,-1,0.004,269.2923],[-0.0052,0.003,1,3071.5]])


B2C = row_stack((exMatrix,[0,0,0,1]))

C2W = tranMatrix_B2W.dot(B2C.I)
'''
#print(C2W)



#theCompleteMatrix = exMatrix.I.dot(tranMatrix)

#print(theCompleteMatrix)

camer_Test = mat([2936.903,2253.801,0,1])

print("++++++++++++++++++++")
#print(C2W.dot(camer_Test.T))
print("++++++++++++++++++++")
#print(tranMatrix.dot(mat([150,150,0,1]).T))

#print("靶坐标：/n",B2C.dot(chess_.T))

'''

#相机坐标系中P点坐标
Camera_p = inMatrix.I.dot(mat([[2936.903,2253.801,1],[2694.531,2251.762,1],[2696.767,2008.884,1],
                          [2407.848,1763.279,1]]).T)


temp = Camera_p[:2, : ]
Camera_p=row_stack((temp,[3050.001,3050.00001,3050.000001,3050.0000001],[0,0,0,1]))
print(Camera_p)
RobotWorld = mat([[2255.3,-206.8,339.5,1],[2256.89,-56.75,338.74,1],[2407.12,-58.54,339.11,1],[2559.62,119.96,339.93,1]])

print("------------------------------------")
C2W = RobotWorld.T.dot(Camera_p.I)
print(C2W)

print("以下是测试：")


Camera_p_test = inMatrix.I.dot(mat([[2792.871,2106.895,1],[2599.246,2056.8,1],[2747.865,1766.76,1]]).T)

temp_test = Camera_p_test[:2,:]
print(temp_test)
Camera_p_test = row_stack((temp_test,[3050.00001,3050.000001,3050.0000001],[0,0,1]))


Robot_Cal = C2W.dot(Camera_p_test)

print("计算结果：")
print(Robot_Cal)


print("下面试海面测试：")

Haimian_test = inMatrix.I.dot(mat([[2102.03,3248.023,1]]).T)
haimian_temp = Haimian_test[:2,:]
print(haimian_temp)

Haimian_test = row_stack((haimian_temp,[3050.0000001],[1]))
Robot_Haimian_Cal = C2W.dot(Haimian_test)
print("计算结果：")
print(Robot_Haimian_Cal)

















































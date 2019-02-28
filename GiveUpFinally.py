#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 18:24
# @Author  : Dongyang
# @Site    : 
# @File    : GiveUpFinally.py
# @Software: PyCharm Community Edition

from numpy import *
import pandas as pd

inMatrix = mat([[4972.66777651433,0,2725.13397174581],
                [0,4971.85881217050,1819.20220316190],
                [0,0,1]])

exMatrix = mat([[-0.999,-0.0098,-0.0052,131.7089],
                [0.0098,-1,0.004,269.2923],
                [-0.0052,0.003,1,3071.5],
                [0,0,0,1]])



RobotWorld = mat([[1897.38,484.17,238.00,1],
                  [2798.95,484.13,241.49,1],
                  [2799.69,-416.08,238.10,1],
                  [1897.28,-417.05,239.30,1]])

Image_uv = mat([[1843.051,2804.07,1],
               [1841.184,1385.322,1],
               [3258.985,1383.457,1],
               [3260.851,2802.204,1]])

Camera_xy = inMatrix.I.dot(Image_uv.T)
Camera_xy = Camera_xy[:2,:]
print(Camera_xy)
Camera_xyz=row_stack((Camera_xy,[3050.001,3050.00001,3050.000001,3050.0000001],[1,1,1,1]))
print(Camera_xyz)

#Matrix_b2w = RobotWorld.T.dot(Camera_xyz.T).dot(exMatrix.I)

#print(Matrix_b2w)
Matrix_c2w = RobotWorld.T.dot(Camera_xyz.I)#求出相机坐标系到世界坐标系的变换矩阵

print("c2w")
print(Matrix_c2w)
#print(tranMatrix)


print("==逆解==")
print(Matrix_c2w.dot(Camera_xyz))

Image_center_uv = mat([[2551.018,2093.763,1]])
Camera_center_xy = inMatrix.I.dot(Image_center_uv.T)
Camera_center_xy = Camera_center_xy[:2,:]

Camera_center_xyz = row_stack((Camera_center_xy,[3050.0000001],[1]))
print(Camera_center_xyz)
print("==验证中心点==")

RobotWorld_Center_xyz = Matrix_c2w.dot(Camera_center_xyz)
print(RobotWorld_Center_xyz)

print("==Image3验证：旋转9度加平移==")

Image3_uv = mat([[3134.144,2710.137,1],
                 [1734.748,2463.844,1],
                 [1980.86,1065.479,1],
                 [3380.256,1311.773,1]])
Camera3_xy = inMatrix.I.dot(Image3_uv.T)
Camera3_xy = Camera3_xy[:2,:]
Camera3_xyz = row_stack((Camera3_xy,[3050.001,3050.00001,3050.000001,3050.0000001],[1,1,1,1]))
RobotWorld3_xyz = Matrix_c2w.dot(Camera3_xyz)
print("验证结果：")
print(RobotWorld3_xyz)

print("==Image4验证：xiao海绵==")

Image4_uv = mat([[1734.343,2509.21,1],
                 [1732.92,1512.003,1],
                 [3284.736,1509.789,1],
                 [3286.158,2506.997,1]])
Camera4_xy = inMatrix.I.dot(Image4_uv.T)
Camera4_xy = Camera4_xy[:2,:]
Camera4_xyz = row_stack((Camera4_xy,[3050.001,3050.00001,3050.000001,3050.0000001],[1,1,1,1]))
RobotWorld4_xyz = Matrix_c2w.dot(Camera4_xyz)
print("4444验证结果：")
print(RobotWorld4_xyz)


print("==Image4验证：大海绵==")

Image5_uv = mat([[1700.006,3237.502,1],
                 [3832.045,3235.994,1],
                 [2764.969,1742.234,1]])
Camera5_xy = inMatrix.I.dot(Image5_uv.T)
Camera5_xy = Camera5_xy[:2,:]
print(Camera5_xy)
Camera5_xyz = row_stack((Camera5_xy,[3050.00001,3050.000001,3050.0000001],[1,1,1]))
RobotWorld5_xyz = Matrix_c2w.dot(Camera5_xyz)
print("5555验证结果：")
print(RobotWorld5_xyz)

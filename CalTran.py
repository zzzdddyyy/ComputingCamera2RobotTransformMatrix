#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 15:17
# @Author  : Dongyang
# @Site    : 
# @File    : CalTran.py
# @Software: PyCharm Community Edition

from numpy import *


camera = mat([[1600.54,47.28,1],[1557.63,3140.76,1],[3030.94,3168.63,1]])

camera_I = camera.I

robot = mat([[-1125.43,1852.93,1],[875.85,1855.57,1],[876.93,2812.42,1]])
tranMatrix = camera_I.dot(robot)
print(tranMatrix)

camera_test = mat([[3090.91,68.6,1]])
camera_test02 = mat([[2320.01,1606.32,1]])

robot_result02 = camera_test02.dot(tranMatrix)
robot_result = camera_test.dot(tranMatrix)

print("第四点坐标：/n",robot_result)
print("="*20)
print("中心点点坐标：/n",robot_result02)
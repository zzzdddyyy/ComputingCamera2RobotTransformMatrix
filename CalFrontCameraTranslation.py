#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 14:22
# @Author  : Dongyang
# @Site    : 
# @File    : CalFrontCameraTranslation.py
# @Software: PyCharm Community Edition

from numpy import *
import pandas as pd

camera = mat([[858.33,1228.96,1],[935.84,2702.81,1],[4030.99,2525.51,1]])

camera_I = camera.I

robot = mat([[2913.4,1132.3,1],[1957.3,1080.5,1],[2067.18,-937.63,1]])
tranMatrix = camera_I.dot(robot)
print(tranMatrix)
df = pd.DataFrame(tranMatrix)
df.to_csv("FrontCameraMatriax",sep=',')

camera_test = mat([[3951.09,1062.14,1]])
camera_Real = mat([[3023.57,-881.04,1]])#Robot坐标
camera_test02 = mat([[2444.06,1879.85,1]])#中心点

robot_result02 = camera_test02.dot(tranMatrix)
robot_result = camera_test.dot(tranMatrix)

print("="*20)
print("="*20)
print("第四点在Robot中实际坐标：/n",camera_Real)
print("="*20)
print("第四点计算坐标：/n",robot_result)
print("="*20)
print("中心点点坐标：/n",robot_result02)
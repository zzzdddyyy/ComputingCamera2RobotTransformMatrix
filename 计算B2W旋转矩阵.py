#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 11:04
# @Author  : Dongyang
# @Site    : 
# @File    : 计算B2W旋转矩阵.py
# @Software: PyCharm Community Edition

from numpy import *

O_ = mat([[2374.70,-282.44,288.02]])#机器人
#O_ = mat([[3052.406,2057.465,3123.09632449639]])
RobotWorld = mat([[2373.41,-102.32,288.01],#X
                  [2374.70, -282.44, 288.02],#O,
                  [2524.97,-281.00,288.00],#Y
                  ])
'''
RobotWorld = mat([[2766.411,2060.245,3123.09632449639],#X
                  [3052.406,2057.465, 3123.0963244963],#O,
                  [3050.265,1771.041,3123.096324496391],#Y
                  ])
                  '''
s1 = 0.0
s2 = 0.0
rx = []
ry = []
print(RobotWorld)
print(RobotWorld[0,0])
for i in range(3):
    print(i)
    rx.append(RobotWorld[0,i] - RobotWorld[1,i])
    s1 += rx[i]**2
    ry.append(RobotWorld[2,i] - RobotWorld[1,i])
    s2 += ry[i]**2
s1 = sqrt(s1)
s2 = sqrt(s2)
for i in range(3):
    rx[i] = rx[i]/s1
    ry[i] = ry[i]/s1

_x = mat(rx)
_y = mat(ry)

print(_x,_y)

_z = cross(_x,_y)

print(_z)

R = row_stack((_x,_y,_z)).T
print(R)
RT = column_stack((R,O_.T.tolist()))
R_T = row_stack((RT,[0,0,0,1]))

print(R_T)


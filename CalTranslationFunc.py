#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 9:38
# @Author  : Dongyang
# @Site    : 
# @File    : CalTranslationFunc.py
# @Software: PyCharm Community Edition

from numpy import *
import pandas as pd

print("请输入图像中第一个角点坐标，eg:*,*,1:")
cordI1 = list(map(int,input().split(',')))
print("请输入图像中第二个角点坐标，eg:*,*,1:")
cordI2 = list(map(int,input().split(',')))
print("请输入图像中第三个角点坐标，eg:*,*,1:")
cordI3 = list(map(int,input().split(',')))

arrayImgCorner = [cordI1,cordI2,cordI3]
imgCorner = mat(arrayImgCorner)

#print(imgCorner)

print("请输入机器人对应中第一个角点坐标，eg:*,*,1:")
cordR1 = list(map(int,input().split(',')))
print("请输入机器人对应第二个角点坐标，eg:*,*,1:")
cordR2 = list(map(int,input().split(',')))
print("请输入机器人中对应第三个角点坐标，eg:*,*,1:")
cordR3 = list(map(int,input().split(',')))

robotCorner = mat([cordR1,cordR2,cordR3])

#逆矩阵
camera_I = imgCorner.I

tranMatrix = camera_I.dot(robotCorner)

df = pd.DataFrame(tranMatrix)
df.to_csv("Camera2RobotMatriaxTest",sep=',')

print("Done！")


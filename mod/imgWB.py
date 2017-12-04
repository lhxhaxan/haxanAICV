#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0
@author: haxan
@license: GUN Licence
@file: imgWB.py
@time: 2017/12/3 11:17
"""

import cv2

def autoGWWB(cvImg):#灰度世界自动白平衡
    krgb = rgbplus(autogary(cvImg))
    print("pp",krgb)
    img = cv2.split(cvImg)
    for i in range(0, len(img)-1):
        for j in range(0, len(img[i])):
            img[i][j] = img[i][j] * krgb[i]
    cvImg = cv2.merge(img)
    return cvImg
    pass

def autogary(cvImg):  # 通过图片计算50%灰度
    krgb = cv2.mean(cvImg)  # 求原始图像的RGB分量的均值 输出krgb[B,G,R,A]
    print("s", krgb)
    return krgb
    pass

def rgbplus(krgb):  # 通过灰度计算每个通道需要增益的比值
    plus = (krgb[0] + krgb[1] + krgb[2]) / 3
    print('p', plus)
    return [
        plus / krgb[0],
        plus / krgb[1],
        plus / krgb[2]
    ]
    pass

class imgWB():
    def __init__(self, imgSource):
        self.gary = [256/2, 256/2, 256/2, 0]  # 50%灰定义值
        self.ugary = []  # 用户50%灰定义值
        self.imgRGB = cv2.split(self.cvimg)
        pass

img = cv2.imread("../sample/timg.jpg")
cv2.imshow("timg", img)
wb =  autoGWWB(img)
cv2.imshow("wb", wb)
print(img,"=============================================================")
print(wb)
cv2.waitKey (0)








if __name__ == '__main__':
    pass
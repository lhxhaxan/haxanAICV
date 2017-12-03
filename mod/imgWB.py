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

def func():
    pass


class imgWB():
    def __init__(self, imgSource):
        self.gary = [256/2, 256/2, 256/2, 0]  # 50%灰定义值
        self.ugary = []  # 用户50%灰定义值
        self.imgRGB = cv2.split(self.cvimg)
        pass

    def __autogary(self, cvImg):  # 通过图片计算50%灰度
        krgb = cv2.mean(cvImg)  # 求原始图像的RGB分量的均值 输出krgb[B,G,R,A]
        return krgb
        pass

    def __rgbplus(self, krgb):  #通过灰度计算每个通道需要增益的比值
        plus = ( krgb[0] + krgb[1] + krgb[2] )/3
        return [
            krgb[0] * plus,
            krgb[1] * plus,
            krgb[2] * plus
        ]
        pass

    def awb(self):
        imgself.cvimg








if __name__ == '__main__':
    pass
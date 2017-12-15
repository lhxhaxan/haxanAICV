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
import numpy as np

def autoGWWB(cvImg):   # 灰度世界自动白平衡
    krgb = rgbplus(autogary(cvImg))
    #print("pp",krgb)
    img = cv2.split(cvImg)
    for i in range(0, 2):
        cv2.addWeighted(img[i],krgb[i],0,0,0,img[i])  # 调整每个通道
    cvImg = cv2.merge(img)  # 合成
    return cvImg
    pass

def autogary(cvImg):  # 通过图片计算50%灰度
    krgb = cv2.mean(cvImg)  # 求原始图像的RGB分量的均值 输出krgb[B,G,R,A]
    #print("s", krgb)
    return krgb
    pass

def rgbplus(krgb):  # 通过灰度计算每个通道需要增益的比值
    plus = (krgb[0] + krgb[1] + krgb[2]) / 3
    #print('p', plus)
    return [
        plus / krgb[0],
        plus / krgb[1],
        plus / krgb[2]
    ]
    pass


def perfectReflector(cvImg, ratio=10 ,maxB=-1):
    img =cv2.split(cvImg)
    wpx = (img[0] + img[1] + img[2]).flatten() #计算像素亮度（升序） flatten，把二维数组转一维数组
    brightest = np.argsort(wpx) # 以亮度排序像素，返回下标（升序）
    #print(brightest[brightest.size * (100 - ratio) //100])
    tap = brightest.size * (100 - ratio) // 100
    for i in range (0,tap)[::-1]: #  包含同一亮度值的像素
        if wpx[brightest[i]] < wpx[brightest[tap]]:
            break
        else:
            tap = i
    RB = np.hsplit(brightest, (0, tap))[2] # 前10%或其他Ratio的白色参考点组成数组，由于升序所以要100-Ratio

    if maxB == -1: # 设定最亮值为图片最亮值
        maxB = wpx[brightest[brightest.size - 1]]

    sumB = 0
    sumG = 0
    sumR = 0
    fimg0 = img[0].flatten()
    fimg1 = img[1].flatten()
    fimg2 = img[2].flatten()
    for element in RB :
        sumB = sumB + fimg0[element]
        sumG = sumG + fimg1[element]
        sumR = sumR + fimg2[element]
    print(sumR, ",", sumG, ",", sumB)
    sizeRB = RB.size
    krgb = [
        maxB / (sumB / sizeRB),
        maxB / (sumG / sizeRB),
        maxB / (sumR / sizeRB)
    ]
    '''
    plusB = 255 / sumB / sizeRB
    plusG = 255 / sumG / sizeRB
    plusR = 255 / sumR / sizeRB
    print(plusB, plusG, plusR)
    '''
    for i in range(0, 2):
        cv2.addWeighted(img[i],krgb[i],0,0,0,img[i])  # 调整每个通道

    cvImg = cv2.merge(img)  # 合成
    return cvImg

class imgWB():
    def __init__(self, imgSource):
        self.gary = [256/2, 256/2, 256/2, 0]  # 50%灰定义值
        self.ugary = []  # 用户50%灰定义值
        self.imgRGB = cv2.split(self.cvimg)
        pass


img = cv2.imread("../sample/timg2.jpg")
cv2.imshow("timg", img)
wb =  autoGWWB(img)
cv2.imshow("wb", wb)
print(img,"=============================================================")
print(wb)
wb2 = perfectReflector(img, 1, 220)
cv2.imshow("wb2", wb2)
print(img,"=============================================================")
print(wb2)
cv2.waitKey (0)





if __name__ == '__main__':
    pass
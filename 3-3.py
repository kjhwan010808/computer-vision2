# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:41:29 2024

@author: os
"""

import cv2 as cv
import sys
 
img = cv.imread("C:/Users/os/Downloads/soccer.jpg")

t, bin_img = cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임계값=', t)

cv.imshow('R channel', img[:,:,2])
cv.imshow('R channel binarization', bin_img)
          
cv.waitKey()
cv.destroyAllWindows()
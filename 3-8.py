# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:35:23 2024

@author: os
"""

import cv2 as cv

img = cv.imread("C:/Users/os/Downloads/rose.png")

patch = img[255:350, 170:270, : ]

img = cv.rectangle(img, (170,250), (270,350), (255,0,0), 3)

patch1 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)


cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()
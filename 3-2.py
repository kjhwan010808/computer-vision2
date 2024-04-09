# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:31:25 2024

@author: os
"""


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("C:/Users/os/Downloads/soccer.jpg");

h = cv.calcHist([img], [2], None,[256],[0,256])
plt.plot(h, color='r', linewidth=1)

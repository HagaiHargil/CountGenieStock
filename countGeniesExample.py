# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:28:02 2016

@author: Hagai
"""
from __future__ import division
from __future__ import print_function
import cv2
import numpy as np

#%% File IO
fileName = 'IMG_1563.JPG'

#%% Show basic image in grayscale (that's the '0' in imread)
img = cv2.imread(fileName, 0)
cv2.imshow('Source Image', img)

#%% Smoothing and blurring the image to get rid of possible overlapping circles
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#%% Run Hough circle transform
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp=1,minDist=85,
                            param1=50,param2=30,minRadius=85,maxRadius=150)
circles = np.uint16(np.around(circles))

#%% Show and save data
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow(fileName,cimg)
cv2.imwrite('Circled_' + fileName, cimg)

#%% Display text
numOfCircles = circles.shape[1]

print('I found', numOfCircles, 'circles.')


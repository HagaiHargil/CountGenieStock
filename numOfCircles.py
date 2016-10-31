# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:31:03 2016

Receive an image and return the number of circles detected in it.

@author: Hagai Hargil
"""

from __future__ import division
from __future__ import print_function
import cv2

def numOfCircles(img, minRad=20, maxRad=60):
    #%% Smoothing and blurring the image to get rid of possible overlapping circles
    img = cv2.medianBlur(img,5)
    
    #%% Run Hough circle transform
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp=1,minDist=minRad,
                                param1=50,param2=30,minRadius=minRad,maxRadius=maxRad)
    try:
        numOfDetectedCircles = circles.shape[1]
        return numOfDetectedCircles
    except AttributeError: # when circles is empty
        return -1
    
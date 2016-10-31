# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:37:57 2016

@author: Hagai
"""

import numpy as np

def findStableFrame(curFrame, prevFrame):
    '''
    Takes two frames and checks their difference. Only stable frames should be
    checked for circle numbers. Threshold should be changed with experience.
    '''
    threshold = 25 # this works with the single video I received
    if prevFrame == []: 
        return False # initialization will not create a circle analysis
        
    dist = np.sum((curFrame.astype("float") - prevFrame.astype("float")) ** 2)
    dist /= float(curFrame.shape[0] * curFrame.shape[1])
    
    if dist < threshold:
        return True # meaning frames are similar and we should analyze circles
    else:
        return False
        
    
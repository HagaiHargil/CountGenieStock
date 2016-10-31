# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:39:17 2016

@author: Hagai
"""

import findTheDrawer
import cv2
from findStableFrame import findStableFrame

def main(drawerNum, fileName):
    '''
    Receives the drawer and the movie filename (or deviceID) and runs the script
    over the full video file. Returns the difference between starting and ending 
    Genie packs in the frame.
    '''
    movieObject = cv2.VideoCapture(fileName) # you can also write here the device index and the camera should start automatically
    numOfGenies = list() 
    frameLeaps = 10 # no need to check every frame, once every 10 frames (~0.4 sec) seems enough
    frameNum = 1
    prevFrame = []
    ret, frame = movieObject.read() # first frame of video
    while ret: # file still open
        if (frameNum % frameLeaps == 0) and ret == True: # every x frames analyze a frame
            isStableFrame = findStableFrame(frame[:,:,0], prevFrame[:,:,0]) # Decides if it should check for amount of circles
            if isStableFrame:
                numOfGenies.append(findTheDrawer.ChoiceManager().process(drawerNum, frame[:,:,0])) # count the circles and store in list
        prevFrame = frame
        ret, frame = movieObject.read() # we read the video rame by frame
        frameNum += 1
        
    movieObject.release() # this will close the camera if it was opened by cv2.VideoCapture
    cv2.destroyAllWindows()
    
    if not numOfGenies: 
        raise ValueError("numOfGenies is empty. Couldn't determine number of grabbed Genies.")
    else:
        lastValue = numOfGenies[-1]
        n = -2
        while lastValue == -1: # will get rid of -1 generated when no circles were found
            lastValue = numOfGenies[n]
            n -= 1
            
        return max(numOfGenies) - lastValue # the maximum of the list is the most circles it could find.
        # the last place in the list is the last frame in which it could count circles.

#%%
if __name__ == '__main__': # just for debugging purposes
    fileName = 'WIN_20161030_14_22_09_Pro.mp4'
    drawerNum = '2' # the signal from the right drawer goes in here (as a string)
    grabbedGenies = main(drawerNum, fileName)
    print('A total of', grabbedGenies, 'Genie(s) were grabbed this time.')
    
    
    
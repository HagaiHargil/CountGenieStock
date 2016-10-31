# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 12:15:56 2016

@author: Hagai
"""
from __future__ import division
from __future__ import print_function
from numOfCircles import numOfCircles

class ChoiceManager:
    '''
    A class that functions as a replacement for switch-case statements. Depending
    on the drawer number that was opened, it calls the function that counts the
    Genies with the right minimum and maximum possible radius values. This allows
    us to disregard depth issues. 
    Currently implemented for 7 drawers. If there are more - just add another case.
    '''
    def __init__(self):
        self.__choice_table = \
        {
            "1" : self.countGeniesDrawer1,
            "2" : self.countGeniesDrawer2,
            "3" : self.countGeniesDrawer3,
            "4" : self.countGeniesDrawer4,
            "5" : self.countGeniesDrawer5,
            "6" : self.countGeniesDrawer6,
            "7" : self.countGeniesDrawer7,
        }

    def countGeniesDrawer1(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 85
        maxRad = 115
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans
        
    def countGeniesDrawer2(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 80
        maxRad = 105
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans
        
    def countGeniesDrawer3(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 75
        maxRad = 100
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans
        
    def countGeniesDrawer4(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 70
        maxRad = 95
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans
        
    def countGeniesDrawer5(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 60
        maxRad = 90
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans

    def countGeniesDrawer6(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 55
        maxRad = 85
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans

    def countGeniesDrawer7(self, img):
        '''
        Calls the counting function with suitable radii values.
        '''
        minRad = 50
        maxRad = 80
        missingCans = numOfCircles(img.astype('uint8'), minRad, maxRad)
        return missingCans
        
    def process(self, drawerNum, img):
        '''
        Call the right case in the dictionary defined in choice_table.
        '''
        missingCans =  self.__choice_table[drawerNum](img)
        return missingCans
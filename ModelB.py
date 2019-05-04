# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:16:17 2019

@author: Bartek

CMD:
C:/Users/Bartek/Anaconda3/Scripts
pip install -U pygame --user
restart spyder


Model teoretycznie działa ale trzeba go ładnie wyswietlić, zrobię to jutro



"""






import numpy as np
#import pygame

#pygame.init()

gridsize=50

dff=0.05 #ile zanieczyszczeń przechodzi na sąsiadującą kratkę
sd=0.99  #ile zanieczyszczeń pozostaje w cyklu

#źródła
sources=np.zeros((gridsize,gridsize))
sources[25][25]=100




grid=np.zeros((gridsize,gridsize))



for abdas in range(10):
    gridn=np.zeros((gridsize,gridsize))

    
    grid=grid

    # add pollution from sources to new grid    
    gridn+=sources
    
    
    #spread old pollution and...
    #reduce pollution from old grid because it disapears over time
    
    
    
    for x in range(1,gridsize-1):
        for y in range(1,gridsize-1): # sorces + remaining pollution from previous cycle (spreaded pollution)
            gridn[x-1][y]=gridn[x][y]+sd*(dff*(grid[x-1][y]+grid[x+1][y]+grid[x][y-1]+grid[x][y+1])+(1-dff)*grid[x][y])
    


        
        
        
        
    grid=gridn


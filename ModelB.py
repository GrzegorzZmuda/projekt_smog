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





import time
import numpy as np
import os

import pygame
from pygame import surfarray
from pygame.locals import *
from numpy import int32
pygame.init()
from chart import chart
Max = 2000
Xmax=Max/6
gridsize=50
scale=8


dff=0.20 #ile zanieczyszczeń przechodzi na sąsiadującą kratkę
sd=0.999  #ile zanieczyszczeń pozostaje w cyklu

#źródła
sources=np.zeros((gridsize,gridsize))
sources[25][25]=1000


def convert1(temp):
    temp=Max-temp/10
    if (temp>500):
        red= 1000-temp
    else:
        red=0
    green=abs(temp-500)
    
    if temp<500:
        blue=temp
    else:
        blue=0
    return (red*255/500,green*255/500,blue*255/500)


def convert(temp):
    temp=temp/Xmax
    c=1
    x=1-abs(temp % 2 - 1)
    #"""
    if(temp<1):
        return (255,x*255,0)
    elif(temp<2):
        return (x*255,255,0)
    elif(temp<3):
        return (0,255,x*255)
    elif(temp<4):
        return (0,x*255,255)
    elif(temp<5):
        return (x*255,0,255)
    elif(temp<6):
        return (255,0,x*255)
    else:
        return(255,255,255)
    """
    
    if(temp<1):
        return (255,0,x*255)
    elif(temp<2):
        return (x*255,0,255)
    elif(temp<3):
        return (0,x*255,255)
    elif(temp<4):
        return (0,255,x*255)
    elif(temp<5):
        return (x*255,255,0)
    elif(temp<6):
        return (255,x*255,0)
    else:
        return(255,255,255)

    """

def sinit(data) :
    #return 0
    screen=pygame.display.set_mode((data.shape[0]*scale,data.shape[1]*scale))
    pygame.display.flip()
    return screen

def show (data,screen) :    
    #screen = pygame.display.set_mode((data.shape[0]*scale,data.shape[1]*scale), 0, 32)
    img= np.zeros((data.shape[0],data.shape[1],3))
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
                img[x,y,:]=convert(data[x,y])
   
    
    
    surfarray.blit_array(screen, img.repeat(scale,axis=0).repeat(scale,axis=1))
   
    
    
    pygame.display.set_caption("test")
    """
    while 1:
        e = pygame.event.wait()
        if e.type == MOUSEBUTTONDOWN: break
        elif e.type == QUIT:
            pygame.quit()
            raise SystemExit()
    """
    
    pygame.display.update()

grid=np.zeros((gridsize,gridsize))
screen=sinit(grid);


for abdas in range(400):
    gridn=np.zeros((gridsize,gridsize))

    
    grid=grid

    # add pollution from sources to new grid    
    gridn+=sources
    
    
    #spread old pollution and...
    #reduce pollution from old grid because it disapears over time
    
    
    
    for x in range(1,gridsize-1):
        for y in range(1,gridsize-1): # sorces + remaining pollution from previous cycle (spreaded pollution)
            gridn[x][y]=gridn[x][y]+sd*(dff*(grid[x-1][y]+grid[x+1][y]+grid[x][y-1]+grid[x][y+1])+(1-(dff*4))*grid[x][y])

    #chart(grid, gridsize, gridsize)
    grid=gridn

    show(grid,screen)

pygame.quit()

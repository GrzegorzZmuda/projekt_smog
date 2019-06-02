# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:16:17 2019

@author: Bartek

CMD:
C:/Users/Bartek/Anaconda3/Scripts
pip install -U pygame --user
restart spyder

"""


import time
import numpy as np
import os

import pygame
from pygame import surfarray
from pygame.locals import *
from numpy import int32



def init(xDim,yDim,valmax=2000,scscale=8):
    global screen
    global scale
    global vmax
    global xdim
    global ydim
    xdim=xDim
    ydim=yDim
    vmax = valmax/6
    scale = scscale
    pygame.init()
    screen = pygame.display.set_mode((xdim*scale,ydim*scale))
    pygame.display.flip()
    
    
def show (data) :    
    global screen
    img= np.zeros((xdim,ydim,3))
    for x in range(xdim):
        for y in range(ydim):
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




def convert(temp):
    temp=(temp/vmax)
    x=1-abs((temp) % 2 - 1)
    
    if(temp<1):
        return (0,x*255,255) #Blue - lb
    elif(temp<2):
        return (0,255,x*255) #lb - Green
    elif(temp<3):
        return (x*255,255,0) #green - yellow
    elif(temp<4):
        return (255,x*255,0) #yellow - red
    elif(temp<5):
        return (255,0,x*255) #red - purple
    elif(temp<6):
        return (255,x*255,255) # purple - white
    else:
        return(255,255,255)


def quit():
    pygame.quit()



def showlist(ls):
    del ls[(xdim*ydim):]
    y=np.transpose(np.asarray(ls).reshape(xdim,ydim))
    show(y)
    
    
def dispall(data): # wyswietl po klatkach
    showlist(data[0])#wyswietl 1
    i=0
    while(1): #główna pętla
        e = pygame.event.wait()        
        if e.type == KEYDOWN and e.key == K_LEFT:
            if (i<len(data)):
                i=i+1
        elif e.type == KEYDOWN and e.key == K_RIGHT:
            if (i>0):
                i=i-1
        elif e.type == QUIT:
            break;
        showlist(data[i])#wyswietl 1
    
    
    
    
    
    
"""

if __name__ == '__main__':
    main()
    
"""
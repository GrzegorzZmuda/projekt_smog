# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:27:09 2019

@author: pichi
"""

def windangle(w):
    res=[]
    di=0
    for i in w:
        if (i=="N"):
            res.append(0)
        elif (i=="E"):
            res.append(90)
        elif (i=="S"):
            res.append(2*90)
        elif (i=="W"):
            res.append(90)
            di=1    
    r= statistics.mean(res)
    if (di==1):
        r=360-r
        print("W")
    return r

print (windangle("NNE"))
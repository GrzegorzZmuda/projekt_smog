# -*- coding: utf-8 -*-
"""
Created on Thu May  9 03:34:40 2019

czyta położenie stacji + podgląd ich rozkładu

@author: pi
"""

import xlrd
import matplotlib.pyplot as plt


s = xlrd.open_workbook('dane/MetadaneKrk.xls')
stacje = s.sheet_by_index(0)

w, h = 3, 12;
res = [[0 for x in range(w)] for y in range(h)] #w tym jest zapisane id i koordynaty

for i in range (12):
    print(stacje.cell(i, 1).value,stacje.cell(i, 14).value,stacje.cell(i, 15).value)
    res[i][0]=stacje.cell(i, 1).value
    res[i][1]=stacje.cell(i, 14).value
    res[i][2]=stacje.cell(i, 15).value
    
    
    plt.scatter(res[i][1],res[i][2])
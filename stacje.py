# -*- coding: utf-8 -*-
"""
Created on Thu May  9 03:34:40 2019

czyta położenie stacji + podgląd ich rozkładu + rozmiar zależny od poziomu PM10 dnia 01.01.2017

@author: pi
"""

import xlrd
import matplotlib.pyplot as plt


s = xlrd.open_workbook('dane/MetadaneKrk.xls')
stacje = s.sheet_by_index(0)

p = xlrd.open_workbook('dane/2017_PM10_1g.xlsx')
pm10 = p.sheet_by_index(0)
pc=pm10.ncols

w, h = 4, 12;
res = [[0 for x in range(w)] for y in range(h)] #w tym jest zapisane id i koordynaty

for i in range (12):
    print(stacje.cell(i, 1).value,stacje.cell(i, 14).value,stacje.cell(i, 15).value)
    res[i][0]=stacje.cell(i, 1).value
    res[i][1]=stacje.cell(i, 14).value
    res[i][2]=stacje.cell(i, 15).value
    
    for j in range (pc):
    
        if (pm10.cell(1,j).value == res[i][0] and pm10.cell(6,j).value!=""):
            q=pm10.cell(6,j).value
            res[i][3]=float(q.replace(',', '.'))
        
    
    plt.scatter(res[i][1],res[i][2],s=res[i][3]+10)
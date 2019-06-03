# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:59:43 2019

@author: pichi
"""

import pickle,pogodateraz


with open ('dane/analiza/godz2017.txt', 'rb') as fp:
    godz = pickle.load(fp)
    
with open ('dane/analiza/chmury2017.txt', 'rb') as fp: #chmury - segmenty po 20 punktów procentowych
    chmury = pickle.load(fp)
    
with open ('dane/analiza/opady2017.txt', 'rb') as fp:
    opady = pickle.load(fp)
    
with open ('dane/analiza/temp2017.txt', 'rb') as fp:
    temp = pickle.load(fp)
    
with open ('dane/analiza/wiatrkier2017.txt', 'rb') as fp:
    wiatrkier = pickle.load(fp)
    
with open ('dane/analiza/wiatrpr2017.txt', 'rb') as fp: #wiatrpr - segmenty po 5
    wiatrpr = pickle.load(fp)
    
with open ('dane/analiza/wilg2017.txt', 'rb') as fp:
    wilg = pickle.load(fp)
    
def znajdzwart(lista,x,stacja=0): #wynik: odchylenie stand., srednia]
    j=0
    for l in lista[2][0]:
        if (l==x):
            i=j
            #print(i,len(lista[0]),stacja)
            break
        j=j+1
    
    #print(x,i,lista[0][stacja][i], lista[1][stacja][i] )
    
    return lista[0][stacja][i], lista[1][stacja][i] 

    #[godzina,temperatura, wilgotnosc,zachmurzenie,deszcz(1=tak,0=nie),kierunek wiatru, prędkoć wiatru]

def znajdzwartosci(g,t,w,c,o,k,p,st=0):
    x=[]
    x.append( znajdzwart(godz,g,st) )
    x.append( znajdzwart(temp,t,st) )
    x.append( znajdzwart(wilg,w,st) )
    x.append( znajdzwart(chmury,c,st) )
    x.append( znajdzwart(opady,o,st) )
    x.append( znajdzwart(wiatrkier,k,st) )
    x.append( znajdzwart(wiatrpr,p,st) )
    
    sumasd=0
    
    for i in x:
        sumasd=sumasd+i[0]

    
    r=0
    for i in x:
        r=r+i[1]*(i[0]/sumasd)
    
    return r

#print(znajdzwartosci(10,18,10,20,0,30,10,st=0))
def col(temp):
    
    x=temp/100
    print(temp,x)
    if(temp<10):
        return (0,x*255,255) #Blue - lb
    elif(temp<20):
        return (0,255,x*255) #lb - Green
    elif(temp<30):
        return (x*255,255,0) #green - yellow
    elif(temp<40):
        return (255,x*255,0) #yellow - red
    elif(temp<50):
        return (255,0,x*255) #red - purple
    elif(temp<60):
        return (255,x*255,255) # purple - white
    else:
        return(255,255,255)
    
    
    
    
    
def znajdzteraz():
    pog=pogteraz()
    res=[[] for x in range(8)]
    for q in pog:
        #print(q)
        #print (q[0],znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],0))
        for i in range (len(stacje)):
            res[i].append(znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],i))
           # print(i, znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],i))
           #print(color(znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],i)))
           #plt.scatter(stacje[i][1],stacje[i][2],s=400,c="r",alpha=1.5*(znajdzwartosci(q[0],q[1],q[2],q[3],q[4],q[5],q[6],i)-10)/100)
            
        #plt.figure()
    return res

def zmiany(): #funkcja zwraca zmianę poziomu zanieczyszczeń co godzinę dla 8 stacji przez najbliższe 70 godzin
    res=[[] for x in range(8)]
    p=znajdzteraz()
    
    for i in range(len(p)):
        for j in range(len(p[i])-1):
            res[i].append( p[i][j+1]-p[i][j] )
            
    return res

poziomy=znajdzteraz()
print (znajdzwartosci(23,-20,20,20,0,45,5,0))
print (znajdzwartosci(23,30,20,20,0,45,5,0))
zm=zmiany()
import random

import getwind
import prototyp1
import matplotlib.pyplot as plt

from PolutionAPI import getSensors
from chart import chart

#mapa z wszystkimi kafelkami

import MDisplay as MD
import time
import datetime



class Map:

    #konstruktor
    def __init__(self, x, y):
        self.mid = []
        self.array=[]
        self.xrange=x
        self.yrange=y
        for i in range(x):
            for j in range(y):
                self.array.append(prototyp1.Blok(i,j))
        tmp=getSensors()
        maxlen = 0
        minlen = 360
        maxlat = 0
        minlat = 360
        for i in range(len(tmp)):
            tmplat=tmp[i][0][1]["latitude"]
            tmplen=tmp[i][0][1]["longitude"]


            if( maxlen<tmplen):

                maxlen=tmplen
            if (minlen > tmplen):

                minlen = tmplen

            if (maxlat< tmplat):
                maxlat = tmplat

            if (minlat >tmplat):
                minlat = tmplat



        latdif=abs(maxlat-minlat)
        lendif = abs(maxlen- minlen)
        print(lendif)
        print(latdif)
        if latdif>=lendif:
            self.scale=latdif/(y)

        else:
            self.scale = lendif/(x)

        zerolat=abs(minlat)
        zerolen=abs(minlen)
        for i in range(len(tmp)):
            tmplat = tmp[i][0][1]["latitude"]
            tmplen = tmp[i][0][1]["longitude"]
            xcord=(int(abs(tmplen-zerolen)//self.scale))-1
            ycord=(y-int(abs(tmplat-zerolat)//self.scale))-1


            arrayplace=ycord*self.xrange+xcord

            self.array[arrayplace].set(tmp[i][1]["value"]/30)
            for a in range(x):
                for b in range(y):
                    if self.array[a*x+b].pollution==0:
                        self.array[a*x+b].setchange((tmp[i][1]["value"]/30)/len(tmp))





        for i in range(x):
            for j in range(y):
                self.array[i + j * x].update()
        MD.init(x,y,valmax=1.5)

    #dekonstruktor
    def __del__(self):
        MD.quit()
    
    #wyświetlanie
    def disp(self):
        A=[]
        for i in range(self.yrange):
            for j in range(self.xrange):
                temp = self.array[i*self.xrange+j].disp()
                A.append(temp)
                #print(format(temp, '02f'), end=' ')

            #print()
        self.mid.append(self.array[i * self.xrange + j].disp())
        #chart(A, self.xrange, self.yrange)
        MD.showlist(A)
        time.sleep(0.2)


    #efekt wiatru
    def wind(self,scale=0.1):

        for i in range(self.yrange):
            for j in range(self.xrange):

                temp1 = i * self.xrange + j
                x = self.array[temp1].disp()
                temp2 = x * scale

                if(0<=self.winddeg<90):
                    if (i - 1 >-1):
                        self.array[temp1 - self.xrange].setchange(temp2 * self.windspeed * scale*(self.winddeg/90))
                    if (j + 1< self.xrange):
                        self.array[temp1 + 1].setchange(temp2 * self.windspeed * scale*(1-(self.winddeg/90)))
                    self.array[temp1].setchange(-(temp2 * self.windspeed * scale*(1-(self.winddeg/90)))-temp2 * self.windspeed * scale*(self.winddeg/90))
                elif (90<= self.winddeg < 180):
                    if (j + 1< self.xrange):
                        self.array[temp1 + 1].setchange(temp2 * self.windspeed * scale*((self.winddeg-90)/90))
                    if (i + 1< self.yrange):
                        self.array[temp1 + self.xrange].setchange(temp2 * self.windspeed * scale*(1-(self.winddeg-90)/90))
                    self.array[temp1].setchange(-(temp2 * self.windspeed * scale * (1 - ((self.winddeg-90)/ 90)))
                                                - temp2 * self.windspeed * scale * ((self.winddeg-90)/ 90))
                elif (180 <= self.winddeg < 270):
                    if (i + 1< self.yrange):
                        self.array[temp1 + self.xrange].setchange(temp2 * self.windspeed * scale*((self.winddeg-180)/90))
                    if (j - 1 > -1):
                        self.array[temp1 - 1].setchange(temp2 * self.windspeed * scale*(1-(self.winddeg-180)/90))
                    self.array[temp1].setchange(-(temp2 * self.windspeed * scale * (1 - ((self.winddeg - 180) / 90)))
                                                - temp2 * self.windspeed * scale * ((self.winddeg - 180) / 90))
                else:
                    if (j - 1 > -1):
                        self.array[temp1 - 1].setchange(temp2 * self.windspeed * scale*((self.winddeg-270)/90))
                    if (i - 1 > -1):
                        self.array[temp1 - self.xrange].setchange(temp2 * self.windspeed * scale*(1-(self.winddeg-270)/90))
                    self.array[temp1].setchange(-(temp2 * self.windspeed * scale * (1 - ((self.winddeg - 270) / 90)))
                                                - temp2 * self.windspeed * scale * ((self.winddeg - 270) / 90))


    #symulacja rozprzestrzeniania się smogu(beZ wiatru)
    def spread(self,scale):
        #kalkulowanie zmian
        for i in range(self.yrange):
            for j in range(self.xrange):
                temp1=i*self.xrange+j

                x=self.array[temp1].disp()
                temp2 = x * scale
                if(j-1>-1):
                    self.array[temp1-1].setchange(temp2)

                if (j + 1 < self.xrange):
                    self.array[temp1 + 1].setchange(temp2)

                if (i - 1 > -1):
                    self.array[temp1 - self.xrange].setchange(temp2)

                if (i + 1 < self.yrange):
                    self.array[temp1 + self.xrange].setchange(temp2)

                self.array[temp1].setchange(-temp2*4)

    #update kafelek
    def update(self):
        for i in range(self.yrange):
            for j in range(self.xrange):
                self.array[i*self.xrange+j].update()

    #jeden cykl symulacji
    def cycle(self,spreadscale):
        self.spread(spreadscale)
        self.car()
        self.emmision()
        self.wind()
        self.update()
        self.disp()
        print()

    #spreadscale - prędkość rozprowadzanie sie zanieczyszczeń
    #length- ilość cykli
    #starthour - godzina rozpoczecia
    def simulate(self,spreadscale=0.01,length=72,):
        tmp=getwind.weathernow()
        self.windspeed=tmp[0]
        self.winddeg = tmp[1]
        now = datetime.datetime.now()
        self.hour=now.hour
        self.midyaxis=[]
        for i in range(length):
            self.midyaxis.append(i+1)
            self.cycle(spreadscale)
            self.hour+=1
            if(self.hour>24):
                self.hour=0

        plt.plot(self.midyaxis,self.mid)
        plt.show()



    #bazowa emisja (mieszkania)
    def emmision(self, amount=0.6):
        if(18>self.hour>24):
            for i in range(self.yrange):
                for j in range(self.xrange):
                    self.array[i * self.xrange + j].setchange(amount)


    #bazowa emisja (samochody)
    def car(self, amount=0.03):
        if ((15 < self.hour < 18) or (6 < self.hour < 9)):
            for i in range(self.yrange):
                for j in range(self.xrange):
                    self.array[i * self.xrange + j].setchange(amount)





#symulacja
a=Map(40,40)
a.simulate()
del a
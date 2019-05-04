import random
import prototyp1
import matplotlib.pyplot as pl

#mapa z wszystkimi kafelkami
class Map:

    #konstruktor
    def __init__(self, x, y):
        self.mid = []

        self.array=[]
        self.xrange=x
        self.yrange=y
        for i in range(x):
            for j in range(y):
                self.array.append(prototyp1.Blok(i,j,random.randrange(4,7)))

    #wyświetlanie (tymczasowo/ później trzeba bedzie zrobić wersje graficzną)
    def disp(self):

        for i in range(self.yrange):
            for j in range(self.xrange):
                temp = self.array[i*self.xrange+j].disp()
                print(format(temp, '02f'), end=' ')

            print()
        self.mid.append(self.array[i * self.xrange + j].disp())

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
        self.update()
        self.disp()
        print()

    #spreadscale - prędkość rozprowadzanie sie zanieczyszczeń
    #length- ilość cykli
    #starthour - godzina rozpoczecia
    def simulate(self,spreadscale=0.1,length=96,starthour=0):
        self.hour=starthour
        self.midyaxis=[]
        for i in range(length):
            self.midyaxis.append(i+1)
            self.cycle(spreadscale)
            self.hour+=1
            if(self.hour>24):
                self.hour=0

        pl.plot(self.midyaxis,self.mid)
        pl.show()



    #bazowa emisja (mieszkania)
    def emmision(self, amount=0.5):
        if(15>self.hour>20):
            for i in range(self.yrange):
                for j in range(self.xrange):
                    self.array[i * self.xrange + j].setchange(amount)


    #bazowa emisja (samochody)
    def car(self, amount=0.25):
        if ((15 < self.hour < 18) or (6 < self.hour < 9)):
            for i in range(self.yrange):
                for j in range(self.xrange):
                    self.array[i * self.xrange + j].setchange(amount)

#symulacja
a=Map(3,3)
a.simulate()

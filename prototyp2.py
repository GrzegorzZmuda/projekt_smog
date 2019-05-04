import random
import prototyp1


#mapa z wszystkimi kafelkami
class Map:
    #konstruktor
    def __init__(self, x, y):
        self.array=[]
        self.xrange=x
        self.yrange=y
        for i in range(x):
            for j in range(y):
                self.array.append(prototyp1.Blok(i,j,random.randrange(1,10)))

    #wyświetlanie (tymczasowo/ później trzeba bedzie zrobić wersje graficzną)
    def disp(self):
        for i in range(self.yrange):
            for j in range(self.xrange):
                temp = self.array[i*self.xrange+j].disp()
                print(format(temp, '02f'), end=' ')

            print()
    #symulacja rozprzestrzeniania się smogu(beZ wiatru)
    def spread(self):
        #kalkulowanie zmian
        for i in range(self.yrange):
            for j in range(self.xrange):
                temp1=i*self.xrange+j
                temp3=0
                x=self.array[temp1].disp()
                if(j-1>-1):
                    self.array[temp1-1].setchange(x*0.1)
                temp3=temp3- x * 0.1
                if (j + 1 < self.xrange):
                    self.array[temp1 + 1].setchange(x * 0.1)
                temp3 = temp3 - x * 0.1
                if (i - 1 > -1):
                    self.array[temp1 - self.xrange].setchange(x * 0.1)
                temp3 = temp3 - x * 0.1
                if (i + 1 < self.yrange):
                    self.array[temp1 + self.xrange].setchange(x * 0.1)
                temp3 = temp3 - x * 0.1
                self.array[temp1].setchange(temp3)
        #update kafelek
        for i in range(self.yrange):
            for j in range(self.xrange):
                self.array[i*self.xrange+j].update()



a=Map(4,4)
for i in range(5):
    a.disp()
    a.spread()
    print()
a.disp()
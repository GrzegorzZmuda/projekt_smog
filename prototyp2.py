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

                self.array[temp1].setchange(0 - temp2*4)
    #update kafelek
    def update(self):
        for i in range(self.yrange):
            for j in range(self.xrange):
                self.array[i*self.xrange+j].update()

    def cycle(self,scale):
        self.spread(scale)
        self.update()

a=Map(3,3)

for i in range(50):
    #a.disp()
    a.cycle(0.1)


a.disp()
#Bazowa kafelka

class Blok:
    #konstruktor
    def __init__(self, x, y, p=0):
        self.xcord = x
        self.ycord = y      #koordynaty kafelki
        self.pollution = p  #zanieczyszczenie
        self.pollutionchange=0  #zmiana zanieczyszczenia w nastepnej jednostce czasu
    #zwraca zawartość zanieczyszczenia na kafelce
    def disp(self):
        return self.pollution
    #ustawia zmiane wartości zanieczyszczenia
    def setchange(self,x):
        self.pollutionchange=self.pollutionchange+x
    #update kafelki
    def update(self):
        self.pollution=self.pollution+self.pollutionchange
        self.pollutionchange=0


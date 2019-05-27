#Bazowa kafelka

class Blok:
    #konstruktor
    def __init__(self, x, y, p=0,type=1):
        self.type = type #typ kafelki
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
        self.pollution+=self.pollutionchange
        self.pollution=self.pollution*0.993
        self.pollutionchange=0


class Blok:

    def __init__(self, x, y, p=0):
        self.xcord = x
        self.ycord = y
        self.pollution = p
        self.pollutionchange=0

    def disp(self):
        return self.pollution

    def setchange(self,x):
        self.pollutionchange=self.pollutionchange+x

    def update(self):
        self.pollution=self.pollution+self.pollutionchange
        self.pollutionchange=0


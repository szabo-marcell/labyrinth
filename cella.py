
class Cella:
    def __init__(self,fent:bool,jobb:bool,lent:bool, bal:bool):
        self.falak= {'fel': 1 if fent else 0, 'jobb': 1 if jobb else 0, 'le': 1 if lent else 0,
                     'bal': 1 if bal else 0}
    def falszam(self):
        return self.falak['fel']+self.falak['le']+self.falak['bal']+self.falak['jobb']

    @property
    def jobb(self):
        return self.falak['jobb']

    @property
    def fel(self):
        return self.falak['fel']

    @property
    def bal(self):
        return self.falak['bal']

    @property
    def le(self):
        return self.falak['le']

    def vanFal(self,irany:str):
        return self.falak[irany]

    @property
    def falak(self):
        return self._falak

    def __str__(self):
        result = ''
        if self.falak['fel'] == 1: result += 'F'
        if self.falak['jobb'] == 1: result += 'J'
        if self.falak['le'] == 1: result += 'L'
        if self.falak['bal'] == 1: result += 'B'
        return result

    @falak.setter
    def falak(self, value):
        self._falak = value

    def falListaba(self)->list:
        return [self.fel, self.jobb, self.le, self.bal]


#print(Cella(True,True,False,False))


class Cella:
    def __init__(self,fent:bool,jobb:bool,lent:bool, bal:bool):
        self.falak= {'fent': 1 if fent else 0, 'jobb': 1 if jobb else 0, 'lent': 1 if lent else 0,
                     'bal': 1 if bal else 0}
    def falszam(self):
        return self.falak['fent']+self.falak['lent']+self.falak['bal']+self.falak['jobb']

    @property
    def jobb(self):
        return self.falak['jobb']

    @property
    def fent(self):
        return self.falak['fent']

    @property
    def bal(self):
        return self.falak['bal']

    @property
    def lent(self):
        return self.falak['lent']

    @property
    def falak(self):
        return self._falak

    def __str__(self):
        result = ''
        if self.falak['fent'] == 1: result += 'F'
        if self.falak['jobb'] == 1: result += 'J'
        if self.falak['lent'] == 1: result += 'L'
        if self.falak['bal'] == 1: result += 'B'
        return result

    @falak.setter
    def falak(self, value):
        self._falak = value


print(Cella(True,True,False,False))


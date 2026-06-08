class Labirintus:
    def __init__(self):
        self.tabla=[]

    def __str__(self):
       for i in range(len(self.tabla)):
           for j in range(len(self.tabla[0])):
               print(self.tabla[i][j].falszam(),end=",")
           print()


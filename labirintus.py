import sys
import turtle
import random

from cella import Cella


class Labirintus:

    def __init__(self):
        self._tabla=[]

    def __init__(self,tabla):
        self._tabla=tabla

    def __init__(self, sorok, oszlopok):
        self._tabla = [[Cella(True, True, True, True)
                       for _ in range(oszlopok)] for _ in range(sorok)]
        latogatott = [[False] * oszlopok for _ in range(sorok)]
        ellentetes = {'fent': 'lent', 'lent': 'fent', 'jobb': 'bal', 'bal': 'jobb'}

        def szomszedok(r, c):
            iranyok = []
            if r > 0 and not latogatott[r-1][c]: iranyok.append(('fent', r-1, c))
            if c < oszlopok-1 and not latogatott[r][c+1]: iranyok.append(('jobb', r, c+1))
            if r < sorok-1 and not latogatott[r+1][c]: iranyok.append(('lent', r+1, c))
            if c > 0 and not latogatott[r][c-1]: iranyok.append(('bal', r, c-1))
            return iranyok

        stack = [(0, 0)]
        latogatott[0][0] = True
        while stack:
            r, c = stack[-1]
            szomszedok_lista = szomszedok(r, c)
            if szomszedok_lista:
                irany, nr, nc = random.choice(szomszedok_lista)
                self.tabla[r][c].falak[irany] = 0
                self.tabla[nr][nc].falak[ellentetes[irany]] = 0
                latogatott[nr][nc] = True
                stack.append((nr, nc))
            else:
                stack.pop()

    

    @property
    def tabla(self):
        return self._tabla


    @tabla.setter
    def tabla(self, ujtabla):
        self._tabla = ujtabla

    def __str__(self):
       for i in range(len(self.tabla)):
           for j in range(len(self.tabla[i])):
               print(self.tabla[i][j].falszam(),end=",")
           print()



def cellaRajzolo(cella:Cella,meret:float):
    falak=cella.falListaba()
    turtle.pendown()
    turtle.color("blue")
    for i in range(4):
        if falak[i]==False:
            turtle.penup()
        turtle.forward(meret)
        turtle.right(90)
        turtle.pendown()

def  labirintusRajzolo(labirintus:Labirintus,meret:float):
    tabla=labirintus.tabla
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            cellaRajzolo(tabla[i][j],meret)
            turtle.penup()
            turtle.forward(meret)
            turtle.pendown()
        turtle.penup()
        turtle.back(len(tabla[i])*meret)
        turtle.right(90)
        turtle.forward(meret)
        turtle.pendown()
        turtle.right(-90)




def main():
    turtle.penup()
    turtle.goto(-200,200)
    turtle.pendown()
    try:
        labirintus=Labirintus(int(sys.argv[1]),int(sys.argv[2]))
    except Exception as e:
        print(e.message)

    labirintusRajzolo(labirintus,40)
    turtle.done()
    gollabirntuscella=ra

if __name__ == '__main__':
    main()

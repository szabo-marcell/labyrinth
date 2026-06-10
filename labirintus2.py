import sys
import turtle
import random

from cella import Cella


class Labirintus:

    def __init__(self, sorok, oszlopok):
        self._tabla = [[Cella(random.choice([True, False]), random.choice([True, False]),
                              random.choice([True, False]), random.choice([True, False]))
                        for _ in range(oszlopok)] for _ in range(sorok)]
        latogatott = [[False] * oszlopok for _ in range(sorok)]
        ellentetes = {'fel': 'le', 'le': 'fel', 'jobb': 'bal', 'bal': 'jobb'}

        def szomszedok(r, c):
            iranyok = []
            if r > 0 and not latogatott[r - 1][c]: iranyok.append(('fel', r - 1, c))
            if c < oszlopok - 1 and not latogatott[r][c + 1]: iranyok.append(('jobb', r, c + 1))
            if r < sorok - 1 and not latogatott[r + 1][c]: iranyok.append(('le', r + 1, c))
            if c > 0 and not latogatott[r][c - 1]: iranyok.append(('bal', r, c - 1))
            return iranyok

        stack = [(0, 0)]
        latogatott[0][0] = True
        while stack:
            if latogatott[sorok - 1][oszlopok - 1]:
                break
            r, c = stack[-1]
            szomszedokLista = szomszedok(r, c)
            if szomszedokLista:
                irany, nr, nc = random.choice(szomszedokLista)
                self.tabla[r][c].falak[irany] = 0
                self.tabla[nr][nc].falak[ellentetes[irany]] = 0
                latogatott[nr][nc] = True
                stack.append((nr, nc))
            else:
                stack.pop()
        for i in range(sorok):
            for j in range(oszlopok):
                if not latogatott[i][j]:
                    for irany in self._tabla[i][j].falak:
                        self._tabla[i][j].falak[irany] = random.choice([0, 1])


    @property
    def tabla(self):
        return self._tabla

    @tabla.setter
    def tabla(self, ujtabla):
        self._tabla = ujtabla

    def __str__(self):
        result = ''
        for i in range(len(self.tabla)):
            for j in range(len(self.tabla[i])):
                result += str(self.tabla[i][j]) + ','
            result += '\n'
        return result


def cellaRajzolo(cella: Cella, meret: float):
    falak = cella.falListaba()
    turtle.pendown()
    turtle.color("blue")
    for i in range(4):
        if falak[i] == False:
            turtle.penup()
        turtle.forward(meret)
        turtle.right(90)
        turtle.pendown()


def labirintusRajzolo(labirintus: Labirintus, meret: float):
    tabla = labirintus.tabla
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            cellaRajzolo(tabla[i][j], meret)
            turtle.penup()
            turtle.forward(meret)
            turtle.pendown()
        turtle.penup()
        turtle.back(len(tabla[i]) * meret)
        turtle.right(90)
        turtle.forward(meret)
        turtle.pendown()
        turtle.right(-90)
    turtle.left(90)
    turtle.forward(len(tabla) * meret)
    turtle.left(-90)


def helyreEro(randi: int, randj: int, meret: float, cel=True):
    turtle.penup()
    turtle.forward(randj * meret + (meret / 2))
    turtle.right(90)
    turtle.forward(randi * meret + (meret / 2))
    if cel:
        turtle.pendown()
        turtle.dot(5, "purple")
        turtle.penup()
        turtle.back(randi * meret + (meret / 2))
    turtle.right(-90)
    if cel:
        turtle.back(randj * meret + (meret / 2))


def lepesMegtetel(lepes: str, meret: float, helyi: int, helyj: int, labirintus: Labirintus, rajzol: bool):
    turtle.tracer(0)
    szogek = {'fel': -90, 'jobb': 0, 'le': 90, 'bal': 180}
    helyzet = {'fel': (-1, 0), 'le': (1, 0), 'jobb': (0, 1), 'bal': (0, -1)}
    turtle.penup()
    if rajzol:
        turtle.pendown()
        turtle.color('red')
        turtle.width(3)
    try:
        if (labirintus.tabla[helyi][helyj]).vanFal(lepes):
            print("Sajnos ebben az irányban fal van!")
            return helyi, helyj
        turtle.right(szogek[lepes])
        helyi += helyzet[lepes][0]
        helyj += helyzet[lepes][1]
        turtle.forward(meret)
        turtle.right(-szogek[lepes])
    except:
        print("Nem létezik olyan irány! Írd be: fel, jobb, le vagy bal.")
    turtle.update()
    return helyi, helyj


def jatek(helyi: int, helyj: int, celi: int, celj: int, labirintus: Labirintus,
          meret: float, rajzol: bool = False):
    print("---A játék elkezdődik.---")
    while (helyi != celi or helyj != celj):
        print("Kérem a következő lépésed! Írd be azt, hogy:(fel,jobb,le vagy bal)!")
        lepes = input().strip().lower()
        helyi, helyj = lepesMegtetel(lepes, meret, helyi, helyj, labirintus, rajzol)
    print("---Vége a játéknak.Elérted a célt.---")


def main():
    sorok = int(sys.argv[1])
    oszlopok = int(sys.argv[2])
    labirintus = Labirintus(sorok, oszlopok)
    print(labirintus)
    try:
        meret = 40.0
        turtle.penup()
        turtle.goto(-200, 200)
        turtle.pendown()
        turtle.tracer(0)
        turtle.update()
        labirintusRajzolo(labirintus, meret)

        celi = sorok - 1
        celj = oszlopok - 1

        turtle.tracer(0)
        helyreEro(celi, celj, meret)
        turtle.update()
        turtle.tracer(0)
        helyreEro(0, 0, meret, False)
        turtle.update()
        jatek(0, 0, celi, celj, labirintus, meret, False)
        turtle.done()

    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()

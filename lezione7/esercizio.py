#Simulazione: La tartaruga e la lepre
from random import randint

class Percorso:

    def __init__(self) -> None:
        
        self.caselle: list = ['-' for _ in range(70)]
        self.meteo: bool = False #se è True c'è il sole, se è False c'è pioggia

class Animale:

    def __init__(self) -> None:
        
        self.casella: int = 1
        self.passo: int = 0
        self.energia = 100



class Tartaruga(Animale):

    def __init__(self) -> None:
        super().__init__()

    def spostamento(self, meteo: bool):

        self.passo = randint(1,10)

        if (self.passo <= 5)and(self.energia >= 5):

            if meteo:
                self.casella += 3
            else:
                self.casella += 2

        elif (self.passo <= 8)and(self.energia >= 10):

            if meteo:
                self.casella += 1

        elif (self.passo <= 10)and(self.energia >= 10):

            if self.casella <= 13:

                self.casella = 1

            else:

                if meteo:
                    self.casella -= 12
                else:
                    self.casella -= 13

        else:

            if (self.energia + 10) > 100:

                self.energia = 100

            else:
                self.energia += 10

class Lepre(Animale):

    def __init__(self) -> None:
        super().__init__()

    def spostamento(self, meteo: bool):

        self.passo = randint(1,10)

        if self.passo <= 2:

            if not(meteo):

                self.casella -= 2


        elif  self.passo <= 4:

            if meteo:
                self.casella += 9
            else:
                self.casella += 7

        elif self.passo <= 5:

            if self.casella <= 13:

                self.casella = 1

            else:

                if meteo:
                    self.casella -= 12
                else:
                    self.casella -= 14

        elif self.passo <= 8:

            if meteo:
                self.casella += 1

            else: 
                self.casella -= 1

        elif self.passo <= 10:

            if self.casella <= 3:

                self.casella = 1

            else:

                if meteo:
                    self.casella -= 2
                else:
                    self.casella -= 4

        else:

            if (self.energia + 10) > 100:

                self.energia = 100

            else:
                self.energia += 10


            
print(f'BANG !!!!! AND THEY\'RE OFF !!!!!')    

tartaruga: Tartaruga = Tartaruga()

lepre: Lepre = Lepre()

percorso: Percorso = Percorso()

count: int = 0

while (tartaruga.casella < 70)and(lepre.casella < 70):

    if (count % 10) == 0:

        percorso.meteo = not(percorso.meteo)

    count += 1

    tartaruga.spostamento(percorso.meteo)
    lepre.spostamento(percorso.meteo)
        

    if (tartaruga.casella == lepre.casella):

        if ('L' in percorso.caselle)and('T' in percorso.caselle):

            percorso.caselle.remove('L')
            percorso.caselle.remove('T')
            percorso.caselle.append('-')

        elif ('OUCH!!!' in percorso.caselle):

            percorso.caselle.remove('OUCH!!!')

        else:

            percorso.caselle.remove('-')

        posizione: int = tartaruga.casella - 1
        percorso.caselle.insert(posizione, 'OUCH!!!')

    else:

        if ('L' in percorso.caselle)and('T' in percorso.caselle):

            percorso.caselle.remove('L')
            percorso.caselle.remove('T')

        elif ('OUCH!!!' in percorso.caselle):

            percorso.caselle.remove('OUCH!!!')
            percorso.caselle.remove('-')

        else:

            percorso.caselle.remove('-')
            percorso.caselle.remove('-')
        
        posizione: int = tartaruga.casella - 1
        percorso.caselle.insert(posizione, 'T')

        posizione: int = lepre.casella - 1
        percorso.caselle.insert(posizione, 'L')


    print(len(percorso.caselle))
    print(f'{percorso.caselle}')


if (tartaruga.casella >= 70)and(lepre.casella >= 70):

    print(f"IT'S A TIE.")

elif tartaruga.casella >= 70:

    print(f"TORTOISE WINS! || VAY!!!")

else:

    print(f'"HARE WINS || YUCH!!!"')
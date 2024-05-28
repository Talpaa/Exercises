#Simulazione: La tartaruga e la lepre
from random import randint

class Percorso:

    def __init__(self) -> None:
        
        self.caselle: list = ['-' for _ in range(70)]
        self.meteo: bool = False #se è True c'è il sole, se è False c'è pioggia
        self.ostacoli: dict = {14: 3, 29: 5, 44: 7}
        self.bonus: dict = {9: 3, 24: 5, 49: 10}

    def add_element(self):

        for key in self.bonus:

            print(key)
            self.caselle.pop(key)
            self.caselle.insert(key, 'bonus')

        for key in self.ostacoli:

            print(key)
            
            self.caselle.pop(key)
            self.caselle.insert(key, 'trap')

        




           

class Animale:

    def __init__(self) -> None:
        
        self.casella: int = 0
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

            self.energia -= 5

        elif (self.passo <= 8)and(self.energia >= 3):

            if meteo:
                self.casella += 1

            self.energia -= 3

        elif (self.passo <= 10)and(self.energia >= 10):

            if self.casella <= 6:

                self.casella = 0

            else:

                if meteo:
                    self.casella -= 6
                else:
                    self.casella -= 7

            self.energia -= 10

        else:

            if (self.energia + 10) > 100:

                self.energia = 100

            else:
                self.energia += 10

        if self.energia < 0:

            self.energia = 0

        elif self.energia > 100:
            
            self.energia = 100

        if self.casella < 0:

            self.casella = 0

class Lepre(Animale):

    def __init__(self) -> None:
        super().__init__()

    def spostamento(self, meteo: bool):

        self.passo = randint(1,10)

        if (self.passo <= 2):

            if not(meteo):

                self.casella -= 2

            if (self.energia + 10) > 100:

                self.energia = 100

            else:

                self.energia += 10


        elif  (self.passo <= 4)and(self.energia >= 15):

            if meteo:
                self.casella += 9
            else:
                self.casella += 7

            self.energia += 15

        elif (self.passo <= 5)and(self.energia >= 20):

            if self.casella <= 12:

                self.casella = 0

            else:

                if meteo:
                    self.casella -= 12
                else:
                    self.casella -= 14

            self.energia -= 20

        elif (self.passo <= 8)and(self.energia >= 5):

            if meteo:
                self.casella += 1

            else: 
                self.casella -= 1

            self.energia -= 5

        elif (self.passo <= 10)and(self.energia >= 8):

            if self.casella <= 2:

                self.casella = 0

            else:

                if meteo:
                    self.casella -= 2
                else:
                    self.casella -= 4

            self.energia -= 8

        if self.energia < 0:

            self.energia = 0

        elif self.energia > 100:
            
            self.energia = 100

        if self.casella < 0:

            self.casella = 0


            
print(f'BANG !!!!! AND THEY\'RE OFF !!!!!')    

tartaruga: Tartaruga = Tartaruga()

lepre: Lepre = Lepre()

percorso: Percorso = Percorso()

percorso.add_element()

count: int = 0

message: str = ''

while (tartaruga.casella < 69)and(lepre.casella < 69):

    if (count % 10) == 0:

        percorso.meteo = not(percorso.meteo)

    count += 1

    tartaruga.spostamento(percorso.meteo)
    lepre.spostamento(percorso.meteo)

    if tartaruga.casella in percorso.ostacoli:

        tartaruga.casella -= percorso.ostacoli[tartaruga.casella]

    elif tartaruga.casella in percorso.ostacoli:

        tartaruga.casella += percorso.ostacoli[tartaruga.casella]

    if lepre.casella in percorso.ostacoli:

        lepre.casella -= percorso.ostacoli[lepre.casella]

    elif tartaruga.casella in percorso.ostacoli:

        lepre.casella += percorso.ostacoli[lepre.casella]
        
    posizione_t: int = tartaruga.casella
    posizione_l: int = lepre.casella


    if (tartaruga.casella == lepre.casella):

        if ('L' in percorso.caselle)and('T' in percorso.caselle):

            var1: int = percorso.caselle.index('L')
            percorso.caselle[var1] = '-'
            
            var2: int = percorso.caselle.index('T')
            percorso.caselle[var2] = '-'

        elif ('OUCH!!!' in percorso.caselle):

            var1 = percorso.caselle.index('OUCH!!!')
            percorso.caselle[var1] = '-'

        else:

            if percorso.caselle[len(percorso.caselle)-1] == '-':
                percorso.caselle.pop(len(percorso.caselle)-1)

            elif percorso.caselle[len(percorso.caselle)-2] == '-':
                percorso.caselle.pop(len(percorso.caselle)-2)

            elif percorso.caselle[len(percorso.caselle)-3] == '-':
                percorso.caselle.pop(len(percorso.caselle)-3)

        percorso.caselle[posizione_t ] = 'OUCH!!!'

    else:

        if ('L' in percorso.caselle)and('T' in percorso.caselle):

            var1 = percorso.caselle.index('L')
            percorso.caselle[var1] = '-'
            
            var2 = percorso.caselle.index('T')
            percorso.caselle[var2] = '-'

        elif ('OUCH!!!' in percorso.caselle):

            percorso.caselle.remove('OUCH!!!')
            
            if percorso.caselle[len(percorso.caselle)-1] == '-':
                percorso.caselle.pop(len(percorso.caselle)-1)

            elif percorso.caselle[len(percorso.caselle)-2] == '-':
                percorso.caselle.pop(len(percorso.caselle)-2)

            elif percorso.caselle[len(percorso.caselle)-3] == '-':
                percorso.caselle.pop(len(percorso.caselle)-3)

        else:
            
            if percorso.caselle[posizione_t] == '-':

                percorso.caselle[posizione_t] = 'T'

            elif percorso.caselle[posizione_t-1] == '-':

                percorso.caselle[posizione_t] = 'T'

            elif percorso.caselle[posizione_t+1] == '-':

                percorso.caselle[posizione_t] = 'T'     


            if percorso.caselle[posizione_l] == '-':
            
                percorso.caselle[posizione_l] = 'L'

            elif percorso.caselle[posizione_l-1] == '-':
            
                percorso.caselle[posizione_l] = 'L'

            elif percorso.caselle[posizione_l+1] == '-':
            
                percorso.caselle[posizione_l] = 'L'


    print(len(percorso.caselle))

    for i in percorso.caselle:

        message = message + f'{i} '

    #print(f'Lepre: {lepre.casella}, {lepre.energia}\nTartaruga: {tartaruga.casella}, {tartaruga.energia}')
    print(f'{message}\n')

    message = ''


if (tartaruga.casella >= 70)and(lepre.casella >= 70):

    print(f"IT'S A TIE.")

elif tartaruga.casella >= 70:

    print(f"TORTOISE WINS! || VAY!!!")

else:

    print(f'"HARE WINS || YUCH!!!"')
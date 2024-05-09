class Persona:

    def __init__(self, 
                 nome: str,
                 cognome: str, 
                 data_di_nascita: str,
                 genere: str) -> None:
        
        self.nome: str = nome
        self.cognome: str = cognome
        self.data_di_nascita: int = data_di_nascita
        self.genere: str = genere

    def calcola_età(self):
        pass

persona_1: Persona = Persona(nome = 'Flavio',
                             cognome = 'Giorgi',
                             data_di_nascita = '24/12/94',
                             genere = 'Maschio')

class Dipendente(Persona):

    def __init__(self, nome: str, 
                 cognome: str, 
                 data_di_nascita: str, 
                 genere: str) -> None:
        
        super().__init__(nome, cognome, data_di_nascita, genere)

dipendente_1: Dipendente = Dipendente(nome = 'Flavio',
                             cognome = 'Giorgi',
                             data_di_nascita = '24/12/94',
                             genere = 'Maschio')

print(persona_1.calcola_età())

print(dipendente_1.nome)
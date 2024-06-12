class Specie:

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        self.anni_passati: int = 0

    def cresci(self):
        #Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
        
        self.popolazione = self.popolazione * (1 + self.tasso_crescita/100)

    def anni_per_superare(self, specie: 'Specie')->int:

        self.anni_passati = 0

        while (self.popolazione <= specie.popolazione)and(self.anni_passati <= 1000): 

            self.anni_passati += 1

            self.cresci()
            specie.cresci()
        
        return self.anni_passati
    
    def getDensita(self, area_kmq: float)->int:

        #Formula: popolazione / area_kmq
        
        return int(self.popolazione / area_kmq)
    
class BufaloKlingon(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)

class Elefante(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float, specie: Specie) -> None:
        super().__init__(nome, popolazione, tasso_crescita)
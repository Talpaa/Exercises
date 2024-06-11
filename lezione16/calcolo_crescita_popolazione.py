class Specie:

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        pass

    def anni_per_superare(self)->int:
        pass
    
    def getDensita(self, area_kmq: float)->int:
        pass
    
class BufaloKlingon(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)

class Elefante(Specie):

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float, specie: Specie) -> None:
        super().__init__(nome, popolazione, tasso_crescita)
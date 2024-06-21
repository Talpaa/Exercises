from abc import ABC, abstractmethod

class Forma(ABC):

    @abstractmethod
    def render(self)->str:
        pass

    @abstractmethod
    def getArea(self)->int | float:
        pass


class Quadrato(Forma):

    def __init__(self, lato: int) -> None:

        self.nome: str= 'Quadrato'
        self.lato: int = lato

    def render(self)->str:

        lato: int= self.lato
        message: str = ''

        for i in range(0, lato):

            for j in range(0, lato):

                if (i == 0)or(i == (lato-1)):

                    message += '*'

                elif (j == 0)or(j == (lato-1)):

                    message += '*'

                else:

                    message += ' '

            message += '\n'
        
        return message

    
    def getArea(self)->int:
        
        return self.lato ** 2
    

class Rettangolo(Forma):

    def __init__(self, lato: int, base: int) -> None:
        
        self.nome: str = 'Rettangolo'
        self.lato:int = lato
        self.base: int = base

    def render(self) -> str:
        
        lato: int= self.lato
        base: int = self.base
        message: str = ''

        for i in range(0, lato):

            for j in range(0, base):

                if (i == 0)or(i == (lato-1)):

                    message += '*'

                elif (j == 0)or(j == (base-1)):

                    message += '*'

                else:

                    message += ' '

            message += '\n'
        
        return message
    
    def getArea(self) -> int:
        
        return self.lato * self.base
    
class Triangolo(Forma):

    def __init__(self, lato: int, base: int) -> None:

        self.lato: int = lato
        self.base: int = base
        
    def render(self) -> str:
        return super().render()
    
    def getArea(self) -> float:
        
        return (self.lato * self.base) / 2 

quad: Quadrato = Quadrato(4)

print(quad.render())
print(quad.getArea())

ret: Rettangolo = Rettangolo(lato=4, base=3)

print(ret.render())
print(ret.getArea())

tri: Triangolo = Triangolo(lato=7, base=3)

print(tri.render())
print(tri.getArea())

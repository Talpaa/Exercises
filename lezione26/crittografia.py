from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, testoInChiaro: str):
        pass


class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self, testoCodificato: str):
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        
        self.chiave: int = chiave
        self.__alfabeto__: list[str] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']#0-25

    def __spostaCarattere__(self, char: str)->str:
        
        ind: int = self.__alfabeto__.index(char.upper())
        cn: int = ind + self.chiave

        if char.isupper():


            if cn > 25:

                cn = (cn % 25)-1

                char = self.__alfabeto__[cn]

            else:

                char = self.__alfabeto__[ind + self.chiave]

        else:

            if cn > 25:

                cn = (cn % 25)-1

                char = self.__alfabeto__[cn].lower()

            else:

                char = self.__alfabeto__[ind + self.chiave].lower()

        return char

    def codifica(self, testoInChiaro: str)->str:
        
        testoCodificato: str = ''

        for char in testoInChiaro:
            
            if char.upper() in self.__alfabeto__:
                
                testoCodificato += self.__spostaCarattere__(char)

        return testoCodificato
    
    def decodifica(self, testoCodificato: str)->str:
        return super().decodifica()
    

cifrario: CifratoreAScorrimento = CifratoreAScorrimento(chiave= 27)

testoCodificato: str = cifrario.codifica(testoInChiaro='abcdefghijklmnopqrstuvwxyz')

print(testoCodificato)
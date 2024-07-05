class Documento:

    def __init__(self, testo: str) -> None:
        
        self.testo: str = testo

    def setTesto(self, testo: str):

        self.testo = testo

    def getTesto(self)->str:

        return self.testo
    

class Email(Documento):

    def __init__(self, testo: str, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(testo)

        self.mittente: str = mittente
        self.destinatario: str = destinatario
        self.titolo: str = titolo

    def setMittente(self, mittente: str):

        self.mittente = mittente

    def setDestinatario(self, destinatario: str):

        self.destinatario = destinatario

    def setTitolo(self, titolo: str):

        self.titolo = titolo

    def getMittente(self):

        return self.mittente
    
    def getDestinatario(self):

        return self.destinatario
    
    def getTitolo(self):

        return self.titolo
    
    def getTesto(self) -> str:
        
        return f'Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo}\nMessaggio: {self.testo}'
        
    def writeToFile(self):

        with open('documento.txt', 'w') as email:

            email.write(self.getTesto())

class File(Documento):

    def __init__(self, testo: str, percorso: str) -> None:

        self.percorso: str = f'lezione24/documenti/{percorso}.txt'

        super().__init__(self.percorso)
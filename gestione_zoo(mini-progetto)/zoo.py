#controlla se una stringa può essere convertita in float
def is_float(num):

    try:
        float(num)
        return True
    
    except ValueError:

        return False

class Animal:

    #-nome
    #-specie
    #-età
    #-altezza
    #-larghezza
    #-habitat
    #-vita = round(100*(1/età), 3), non è una percentuale
    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 widht: float,
                 preferred_habitat: str,
                 healt: float) -> None:
        
        self.name: str = name
        self.species: str = species

        while (type(age) != int)or(age < 0):
            
            print(f'L\'età inserita non è valida')

            age = input(f'Perfavore inserisci un\'età che deve essere positiva ed intera o zero:     ')

            if age.isdigit():

                age = int(age)
        else:
            self.age: int = age

        while (type(height) != float)or(height <= 0):

            height = input(f'Perfavore inserisci un\'altezza che deve essere maggiore di zero:     ')

            if is_float(height):

                height = float(height)

        else:
            self.height: float = height


        while (type(height) != float)or(height <= 0):

            height = input(f'Perfavore inserisci un\'altezza che deve essere maggiore di zero:     ')

            if is_float(height):

                height = float(height)

        else:
            self.widht: float = widht
            
        self.preferred_habitat: str = preferred_habitat
        self.health: float = healt

    def __str__(self) -> str:
        
        return f'Nome:  {self.name}\n\
Specie: {self.species}\n\
Età: {self.age}\n\
Altezza: {self.height}\n\
Larghezza: {self.widht}\n\
Habitat: {self.preferred_habitat}\n\
Salute: {self.health}'


class Fence:
    
    #-area
    #-temperatura
    #-habitat
    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str,
                 fauna: list = []) -> None:
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.fauna: list = fauna

class ZooKeeper:
    
    #-nome
    #-cognome
    #-id
    def __init__(self,
                 name: str,
                 surname: str,
                 id: str) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id

    


    """Consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
    L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
    ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale."""
    def add_animal(self, animal: Animal, fence: Fence):
        
        occupied_space: float = round(100*(1/(animal.height * animal.widht)), 3)

        if (occupied_space <= fence.area)and(animal.preferred_habitat == fence.habitat):
            
            fence.fauna.append(animal)

            fence.area -= occupied_space

        elif(animal.preferred_habitat != fence.habitat):

            print(f'L\'animale che stai provando ad inserire non è adatto all\'habitat di questo recinto' )

        elif (occupied_space > fence.area):

            print(f'L\'animale che stai provando ad inserire è più grande dell\'area rimasta nel recinto' )

    """Consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
    L'animale viene allontanato dal suo recinto. 
    L'area del recinto viene ripristinata dello spazio che l'animale rimosso occupava."""
    def remove_animal(self, animal: Animal, fence: Fence):
        
        if animal in fence.fauna:

            fence.fauna.remove(animal)

        else:

            print(f'L\'animale che stai provando a rimuovere non è presente in questo recinto')

    """Consente al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    Ogni volta che un animale viene nutrito, la sua salute(health) incrementa di 1% rispetto alla sua salute corrente, 
    e le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
    L'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo."""
    def feed(self, animal: Animal):
        pass

    """Consente al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
    Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""
    def clean(self, fence: Fence)->float:
        pass
    

class Zoo:
    
    #-recinzioni
    #-guardiani dello zoo
    def __init__(self,
                 fence: Fence,
                 zookeeper: ZooKeeper) -> None:
        
        self.fence: Fence = fence
        self.zookeeper: ZooKeeper = zookeeper

    def describe_zoo(self):
        pass



a1: Animal =  Animal('a','b',12,12,13.00,'a',100.00)

print(type(a1.age))
print(a1)
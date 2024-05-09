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
        self.age: int = age
        self.height: float = height
        self.widht: float = widht
        self.preferred_habitat: str = preferred_habitat
        self.health: float = healt


class Fence:
    
    #-area
    #-temperatura
    #-habitat
    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str) -> None:
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat


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
    def add_animal(animal: Animal, fence: Fence):
        
        name: str = input("Inserisci il nome dell'animale: ")
        species: str = input("Inserisci la specie dell'animale: ")


    """Consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
    L'animale viene allontanato dal suo recinto. 
    L'area del recinto viene ripristinata dello spazio che l'animale rimosso occupava."""
    def remove_animal(animal: Animal, fence: Fence):
        pass

    """Consente al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
    Ogni volta che un animale viene nutrito, la sua salute(health) incrementa di 1% rispetto alla sua salute corrente, 
    e le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
    L'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo."""
    def feed(animal: Animal):
        pass

    """Consente al guardiano dello zoo di pulire tutti i recinti dello zoo. 
    Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
    Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata."""
    def clean(fence: Fence)->float:
        pass
    

class Zoo:
    
    #-recinzioni
    #-guardiani dello zoo
    def __init__(self,
                 fence: Fence,
                 zookeeper: ZooKeeper) -> None:
        
        self.fence: Fence = fence
        self.zookeeper: ZooKeeper = zookeeper

    def describe_zoo():
        pass
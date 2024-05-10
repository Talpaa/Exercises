#Daniele Taccini
#controlla se una stringa può essere convertita in float
def is_float(num):

    try:
        float(num)
        return True
    
    except ValueError:

        risposta: bool = False

        if num.isdigit():

            risposta = True

        return risposta

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
                 preferred_habitat: str) -> None:
        
        self.name: str = name
        self.species: str = species

        while (type(age) != int)or(age <= 0):
            
            print(f'\nL\'età dell\'animale inserita non è valida')

            age = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

            if age.isdigit():

                age = int(age)
        else:
            self.age: int = age

        while (not(is_float(height)))or(height <= 0):

            print(f'\nL\'altezza dell\'animale inserita non è valida')

            height = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

            if is_float(height):

                height = float(height)

        else:
            self.height: float = float(height)


        while (not(is_float(widht)))or(widht <= 0):

            print(f'\nLa larghezza dell\'animale inserita non è valida')

            widht = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

            if is_float(widht):

                widht = float(widht)

        else:
            self.widht: float = float(widht)
            
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100*(1/self.age), 3)

    def __str__(self) -> str:
        
        return f'Nome:  {self.name}\n'\
            +f'Specie: {self.species}\n'\
            +f'Età: {self.age}\n'\
            +f'Altezza: {self.height}\n'\
            +f'Larghezza: {self.widht}\n'\
            +f'Habitat: {self.preferred_habitat}\n'\
            +f'Salute: {self.health}\n'


class Fence:
    
    #-area
    #-temperatura
    #-habitat
    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str,
                 fauna: list = []) -> None:
        
        while (not(is_float(area)))or(area <= 0):

            print(f'\nL\'area del recinto inserita non è valida')

            area = input(f'Per favore inserisci un valore numerico che deve essere maggiore di zero:     ')

            if is_float(area):

                area = float(area)

        else:
            self.area: float = float(area)

        while not(is_float(temperature)):

            print(f'\nLa temperatura del recinto inserita non è valida')

            temperature = input(f'Per favore inserisci un valore numerico:     ')

            if is_float(temperature):

                temperature = float(temperature)

        else:
            self.temperature: float = float(temperature)

        self.habitat: str = habitat
        self.fauna: list = fauna

    def __str__(self) -> str:

        message: str = f'Dimensioni recinto: {self.area} metri quadrati\n'\
            +f'Temperatura del recinto: {self.temperature}\n'\
            +f'Habitat del recinto: {self.habitat}\n'\
            +f'Animali nel recinto:\n'
        for animal in self.fauna:

            message += f'\n{animal}'
        
        return message


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
        
        occupied_space: float = round((animal.height * animal.widht), 3)

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
    
    def __str__(self) -> str:
        
        messaggio: str = f'Nome del guardiano dello zoo: {self.name}\n'\
            +f'Cognome del guardiano dello zoo: {self.surname}\n'\
            +f'ID del guardiano dello zoo: {self.id}\n'
        
        return messaggio

class Zoo:
    
    #-recinzioni
    #-guardiani dello zoo
    def __init__(self,
                 fence: Fence,
                 zookeeper: ZooKeeper) -> None:
        
        self.fence: Fence = fence
        self.zookeeper: ZooKeeper = zookeeper

    def describe_zoo(self):
        
        messaggio: str = f'Zoo:\n'

        return messaggio



a1: Animal =  Animal('a', 'b', 1, 12.52, 14, 'a')
a2: Animal =  Animal('a', 'b', 1, 12.52, 14, 'a')
a3: Animal =  Animal('a', 'b', 1, 12.52, 14, 'a')
a4: Animal =  Animal('a', 'b', 1, 12.52, 14, 'a')

print(a1)

f1: Fence = Fence(1000, 10, 'a')

print(f1)


zk1: ZooKeeper = ZooKeeper('a', 'b', '4144')

print(zk1)

zk1.add_animal(animal=a1, fence=f1)
zk1.add_animal(animal=a2, fence=f1)
zk1.add_animal(animal=a3, fence=f1)
zk1.add_animal(animal=a4, fence=f1)

print(f1)
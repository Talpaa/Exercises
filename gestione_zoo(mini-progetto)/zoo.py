#controlla se ciò che è stato passato possa diventare float
def is_float(num):

    try:
        float(num)
        return True
    
    except ValueError:

        risposta: bool = False

        if num.isdigit():

            risposta = True

        return risposta
    

class Fence:

    def __init__(self, 
                 area: float,
                 temperature: float,
                 habitat: str,
                 fauna: list = []) -> None:
        
        if (not(is_float(area)))or(area <= 0):

            return

        else:
            self.area: float = float(area)

        while not(is_float(temperature)):

            return

        else:
            self.temperature: float = float(temperature)

        self.habitat: str = habitat
        self.remaining_area: float = area
        self.fauna: list = fauna.copy()

    def __str__(self) -> str:

        message: str = ''
    
        if (len(self.fauna) > 0):    

            message = f'\nFence:\n'\
                f'\nFence(area={round(self.area, 3)},temperature: {round(self.temperature, 3)},habitat={self.habitat})\n'\
                    f'\nwith animals:'
            
            for animal in self.fauna:

                message += f'\n{animal}'

            message += f'\n\n******************************'
        
        return message

class Animal:

    def __init__(self,
                 name: str,
                 species: str,
                 age: int,
                 height: float,
                 widht: float,
                 preferred_habitat: str,
                 belong_fence: Fence = '') -> None:
        
        self.name: str = name
        self.species: str = species

        while (type(age) != int)or(age <= 0):
            
            return
        else:
            self.age: int = age

        while (not(is_float(height)))or(height <= 0):

            return

        else:
            self.height: float = float(height)


        while (not(is_float(widht)))or(widht <= 0):

            return

        else:
            self.widht: float = float(widht)
            
        self.preferred_habitat: str = preferred_habitat

        self.health: float = round(100*(1/self.age), 3)

        self.belong_fence: Fence = belong_fence

    def __str__(self) -> str:
        
        return f'\nAnimal(name={self.name},species:{self.species},età:{self.age})'


class ZooKeeper:

    def __init__(self,
                 name: str,
                 surname: str,
                 id: str) -> None:
        
        self.name: str = name
        self.surname: str = surname
        self.id: str = id


    def add_animal(self, 
                   animal: Animal, 
                   fence: Fence):
        
        occupied_space: float = round((animal.height * animal.widht), 3)

        if (occupied_space <= fence.remaining_area)and(animal.preferred_habitat == fence.habitat):
            
            fence.fauna.append(animal)

            fence.remaining_area -= occupied_space

            animal.belong_fence = fence

        return


    def remove_animal(self, 
                      animal: Animal, 
                      fence: Fence):
        
        if animal in fence.fauna:

            occupied_space: float = round((animal.height * animal.widht), 3)

            fence.remaining_area += occupied_space
            fence.fauna.remove(animal)


    def feed(self, 
             animal: Animal):
        
        if animal in animal.belong_fence.fauna:
            increased_height: float = round((animal.height + ((animal.height/100)*2)), 3)
            increased_width: float = round((animal.widht + ((animal.widht/100)*2)), 3)

            dim_re: float = round((animal.belong_fence.remaining_area + (animal.height * animal.widht)), 3)

            increased_animal: float = round((increased_height * increased_width), 3)

            if dim_re >= increased_animal:

                animal.height = increased_height
                animal.widht = increased_width
                animal.health = round((animal.health + (animal.health/100)), 3)


    def clean(self, 
              fence: Fence)->float:
        
        time: float = 0.0

        area_occupata: float = round((fence.area - fence.remaining_area), 3)

        if fence.remaining_area > 0.0:

            time = area_occupata / fence.remaining_area

            return round(time, 3)
        
        else:

            return area_occupata
    
    def __str__(self) -> str:
        
        messaggio: str = f'\nZookeeper(name={self.name},surname={self.surname},id={self.id})'
        
        return messaggio

class Zoo:
    
    def __init__(self,
                 fence: list[Fence] = [],
                 zookeeper: list[ZooKeeper] = []) -> None:
        
        self.fence: list[Fence] = fence
        self.zookeeper: list[ZooKeeper] = zookeeper

    def describe_zoo(self):
        
        messaggio: str = f'Guardians:'

        for i in self.zookeeper:

            messaggio += f'\n{i}'

        for j in self.fence:

            messaggio += f'\n{j}'

        return messaggio

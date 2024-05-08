class Restaurant:

    #-nome
    #-tipo di cunina

    def __init__(self, 
                 name: str, 
                 cuisin_type) -> None:
        
        self.name = name
        self.cuisin_type = cuisin_type

    def describe_restaurant(self):

        print(f'\n\nRistorante\n'\
            + f'Nome: {self.name}\n'\
            + f'Descrizione: {self.cuisin_type}')
        
    def open_restaurant(self):

        print(f'\nIl ristorante {self.name} è aperto')


r1 = Restaurant(name = 'La Vecchia Roma', cuisin_type = 'Romana')

Restaurant.describe_restaurant(r1)

Restaurant.open_restaurant(r1)

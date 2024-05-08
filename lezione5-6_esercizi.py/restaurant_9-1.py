#esercizi 9-1/9-2/9-4
class Restaurant:

    #-nome
    #-tipo di cunina

    def __init__(self, 
                 name: str, 
                 cuisin_type,
                 num_serv: int = 0) -> None:
        
        self.name = name
        self.cuisin_type = cuisin_type
        self.num_serv = num_serv

    def describe_restaurant(self):

        print(f'\n\nRistorante\n'\
            + f'Nome: {self.name}\n'\
            + f'Descrizione: {self.cuisin_type}')
        
    def open_restaurant(self):

        print(f'\nIl ristorante {self.name} è aperto')
 
    def increment_number_served(self, new_num_serv: int)->int:
            
            return (new_num_serv+1)
 
    def set_number_served(self, new_num_serv: int):
        
        self.num_serv = self.increment_number_served(new_num_serv)

        print(f'Stiamo servendo il cliente numero {self.num_serv}')

    


r1 = Restaurant(name = 'La Vecchia Roma', cuisin_type = 'Romana')

r2 = Restaurant(name = 'Dumpling Bar', cuisin_type = 'Cinese')

r3 = Restaurant(name = 'La Cucaracha', cuisin_type = 'Messicana')

Restaurant.describe_restaurant(r1)

Restaurant.describe_restaurant(r2)

Restaurant.describe_restaurant(r3)

Restaurant.open_restaurant(r1)


r1.set_number_served(r1.num_serv)


r1.set_number_served(r1.num_serv)


r1.set_number_served(r1.num_serv)

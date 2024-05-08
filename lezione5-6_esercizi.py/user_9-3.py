class User:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 age: int,
                 cf: str,
                 email: str):
        
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.cf: str = cf
        self.email: str = email

    def greet_user(self):

        return f'\nCiao {self.first_name} {self.last_name}, come stai?'

    def __str__(self) -> str:
        
        return f'\n\nUSER \nName: {self.first_name},\n'\
             + f'Surname: {self.last_name}\n'\
             + f'Age: {self.age}\n'\
             + f'CF: {self.cf}\n'\
             + f'Email: {self.email}'
    
user1 = User('Mario', 'Rossi', 42, 'MRRSS65S67M126L', 'Mario.Rossi@gmail.com')

user2 = User('Luigi', 'Verdi', 37, 'LGVRD65S67M126L', 'Luigi.Verdi@gmail.com')

user3 = User('Rosa', 'Esposito', 54, 'RSSPST65S67M126L', 'Rosa.Esposito@gmail.com')

print(user1)
print(User.greet_user(user1))

print(user2)
print(User.greet_user(user2))

print(user3)
print(User.greet_user(user3))
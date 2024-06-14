from typing import Any

class Persona:

    def __init__(self, first_name: Any, last_name: Any) -> None:
        
        name: bool = False
        surname: bool = False

        if type(first_name) == str:

            self.first_name = first_name
            name = True

        else:

            print(f"Il nome inserito non è una stringa!")
            self.first_name = None

        if type(last_name) == str:

            self.last_name = last_name
            surname = True
            
        else:

            print(f"Il cognome inserito non è una stringa!")
            self.last_name = None

        if name and surname:

            self.age = 0

        else:

            self.age = None

    def setName(self, first_name: Any):

        if type(first_name) == str:

            self.first_name = first_name

        else:

            print(f"Il nome inserito non è una stringa!")

    def setLastName(self, last_name: Any):

        if type(last_name) == str:

            self.last_name = last_name

        else:

            print(f"Il nome inserito non è una stringa!")

    def setAge(self, age: Any):

        if type(age) == int:

            self.age = age

        else:
        
            print(f"L'età inserita non è un intero!")

    def getName(self):

        return f'{self.first_name}'

    def getLastName(self):

        return f'{self.last_name}'

    def getAge(self):

        return f'{self.age}'
    
    def greet(self):

        print(f'Ciao, sono {self.getName()} {self.getLastName()}! Ho età {self.getAge()}!')
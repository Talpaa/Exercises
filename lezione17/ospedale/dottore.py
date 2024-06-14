from typing import Any
from persona import Persona, Any

class Dottore(Persona):

    def __init__(self, first_name: Any, last_name: Any, specialization: Any, parcel: Any) -> None:
        super().__init__(first_name, last_name)

        if type(specialization) == str:

            self.specialization = specialization

        else:

            self.specialization = None

        if type(parcel) == float or type(parcel) == int:

            self.parcel = float(parcel)

        else: 
            self.parcel = None

    def setSpecialization(self, specialization: Any):

        if type(specialization) == str:

            self.specialization = specialization

        else:

            print(f'La specializzazione inserita non è una stringa!')

    def setParcel(self, parcel: Any):

        if type(parcel) == float or type(parcel) == int:

            self.parcel = float(parcel)

        else:

            print(f'Il valore della parcella non è un float!')

    def getSpecialization(self):

        return f'{self.specialization}'

    def getParcel(self):

        return self.parcel
    
    def isAValidDoctor(self):
        
        if self.getAge().isdigit():

            if int(self.getAge()) >= 30:

                print(f"Doctor {self.getName()} e {self.getLastName()} is valid!")

            else:

                print(f"Doctor {self.getName()} e {self.getLastName()} is not valid!")
                
        else:
            
            print(f"Doctor {self.getName()} e {self.getLastName()} is not valid!")
    
    def doctorGreet(self):

        self.greet()

        print(f'Sono un medico {self.getSpecialization()}')


from persona import Persona,Any

class Paziente(Persona):

    def __init__(self, first_name: Any, last_name: Any, id_code: Any) -> None:
        super().__init__(first_name, last_name)

        if type(id_code) == str:

            self.id_code = id_code

        else:

            self.id_code = None

    def setIdCode(self, id_code: Any):

        if type(id_code) == str:

            self.id_code = id_code

        else:

            print(f'L\'id code inserito non è una stringa!')

    def getIdCode(self):

        return f'{self.id_code}'
    
    def patientInfo(self):

        print(f'Paziente: {self.getName()} {self.getLastName()}\n'\
              +f'ID: {self.getIdCode()}')
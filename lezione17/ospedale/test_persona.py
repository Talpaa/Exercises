import unittest

from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class testPersona(unittest.TestCase):

    def setUp(self) -> None:
        
        self.dottore = Dottore(first_name='Claudio', last_name='Pieraccioni', specialization='Neurologo', parcel=538.76)
        self.paziente = Paziente()
        self.fattura = Fattura()

if __name__ == '__main__':
    unittest.main()
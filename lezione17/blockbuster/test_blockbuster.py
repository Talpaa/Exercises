import unittest

from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class testFiml(unittest.TestCase):

    def setUp(self) -> None:
        
        self.film1: Azione = Azione(id= 6384794, title= 'film1')
        self.film2: Azione = Azione(id= 6384794, title= 'film2')
        self.film3: Azione = Azione(id= 6384794, title= 'film3')
        self.film4: Azione = Azione(id= 6384794, title= 'film4')
        self.film5: Azione = Azione(id= 6384794, title= 'fil5')
        self.film6: Commedia = Commedia(id= 6384794, title= 'film6')
        self.film7: Commedia = Commedia(id= 6384794, title= 'film7')
        self.film8: Commedia = Commedia(id= 6384794, title= 'film8')
        self.film9: Commedia = Commedia(id= 6384794, title= 'film9')
        self.film10: Drama = Drama(id= 6384794, title= 'film10')
        self.film11: Drama = Drama(id= 6384794, title= 'film10')


        lista_film: list[Azione, Commedia, Drama] = [self.film1, self.film2, self.film3, self.film4, self.film5, 
                                                     self.film6, self.film7, self.film8, self.film9, self.film10]
        
        self.noleggio: Noleggio = Noleggio(film_list= lista_film)

    def test_isAvailble(self):

        self.assertEqual(first=self.noleggio.isAvaible(film= self.film1),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film1)}\'')
        self.assertEqual(first=self.noleggio.isAvaible(film= self.film11),second=True,msg= f'Error: shoul return \'True\' not \'{self.noleggio.isAvaible(film= self.film11)}\'')

if __name__ == '__main__':
    unittest.main()
import unittest

from my_math_library import FractionError, NoneNumDenError, NullDenominatorError, UnsupportedOperationError, PersonalizedMathLibrary

class TestMyLibrary(unittest.TestCase):

    def setUp(self) -> None:
        
        self.message: str = ''

        self.frazione1: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=12, denominatore=4)
        self.frazione2: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=7, denominatore=1)
        self.frazione3: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=8, denominatore=2)
        self.frazione4: PersonalizedMathLibrary = PersonalizedMathLibrary(numeratore=16, denominatore=7)

    def test_semplifica(self):

        self.message = f'Primo test su semplifica: '
        print(self.message)
        #testa se la funzione semplifica restituisce il numeratore e il denominatore semplificati in modo corretto
        self.assertEqual(first=self.frazione1.semplifica(), second=f'{3.0} {1.0}', msg=f'Error: should return \'3.0 1.0\' not {self.frazione1.semplifica()}')
        self.message = f'Riuscito\n'
        
        self.message += f'Secondo test su semplifica: '
        print(self.message)
        #testa se la funzione non ha niente da semplificare restituisce il numeratore e il denominatore passati
        self.assertEqual(first=self.frazione2.semplifica(), second=f'{7.0} {1.0}', msg=f'Error: should return \'7.0 1.0\' not {self.frazione1.semplifica()}')
        self.message = f'Riuscito\n'
        print(self.message)

    def test_add_fractions(self):

        self.message = f'Primo test su somma fra frazioni: '
        print(self.message)
        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione4), second=f'{148.0} {28.0}', msg=f'Error: should return \'37.0 7.0\' not {self.frazione1.add_fractions(self.frazione4)}') 
        self.message = f'Riuscito\n'
        
        self.message += f'Secondo test su somma fra frazioni: '
        print(self.message)
        #testa che se uno dei due denomitatori è multiplo dell'altro allora il denominatore comune sarà uguale al denominatore multiplo dell'altro
        self.message = f'Riuscito\n'
        
        self.message += f'Terzo test su somma fra frazioni: '
        print(self.message)
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione3), second=f'{28.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.add_fractions(self.frazione3)}')
        self.message = f'Riuscito\n'
        
        self.message += f'Quarto test su somma fra frazioni: '
        print(self.message)
        #testa che se uno dei due denomitatori è 1 il denominatore comune sarà uguale al denominatore non uguale a 1
        self.assertEqual(first=self.frazione1.add_fractions(self.frazione2), second=f'{40.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.add_fractions(self.frazione2)}')
        self.message = f'Riuscito\n'
        print(self.message)

    def test_sub_fractions(self):

        self.message = f'Primo test su somma fra frazioni: '
        print(self.message)
        #testa la funzione add_fraction
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione4), second=f'{148.0} {28.0}', msg=f'Error: should return \'37.0 7.0\' not {self.frazione1.sub_fractions(self.frazione4)}') 
        self.message = f'Riuscito\n'
        
        self.message += f'Secondo test su somma fra frazioni: '
        print(self.message)
        #testa che se uno dei due denomitatori è multiplo dell'altro allora il denominatore comune sarà uguale al denominatore multiplo dell'altro
        self.message = f'Riuscito\n'
        
        self.message += f'Terzo test su somma fra frazioni: '
        print(self.message)
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione3), second=f'{28.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.sub_fractions(self.frazione3)}')
        self.message = f'Riuscito\n'
        
        self.message += f'Quarto test su somma fra frazioni: '
        print(self.message)
        #testa che se uno dei due denomitatori è 1 il denominatore comune sarà uguale al denominatore non uguale a 1
        self.assertEqual(first=self.frazione1.sub_fractions(self.frazione2), second=f'{40.0} {4.0}', msg=f'Error: should return \'28.0 4.0\' not {self.frazione1.sub_fractions(self.frazione2)}')
        self.message = f'Riuscito\n'
        print(self.message)

if __name__ == '__main__':
    unittest.main()
import unittest

from lab_13_weeker import Weeker, WeekDayError

class TestWeeker(unittest.TestCase):

    def test_valid_initialization(self):
        """Testa se a classe inicializa corretamente com um dia válido."""
        weekday = Weeker('Mon')
        self.assertEqual(str(weekday), 'Mon')

    def test_invalid_initialization_raises_error(self):
        """Testa se a classe levanta WeekDayError ao receber um dia inválido."""
        # O assertRaises é perfeito para garantir que o erro esperado acontece!
        with self.assertRaises(WeekDayError):
            Weeker('Monday')

    def test_add_days(self):
        """Testa a lógica circular de adicionar dias."""
        weekday = Weeker('Mon')
        weekday.add_days(15) # Adiciona 15 dias (2 semanas e 1 dia)
        # Se hoje é segunda, daqui a 15 dias tem que ser terça!
        self.assertEqual(str(weekday), 'Tue')
        
        # Mais um teste no mesmo fluxo para garantir
        weekday.add_days(1)
        self.assertEqual(str(weekday), 'Wed')

    def test_subtract_days(self):
        """Testa a lógica circular de subtrair dias."""
        weekday = Weeker('Tue')
        weekday.subtract_days(23) # Subtrai 23 dias (3 semanas e 2 dias)
        # Voltando 23 dias a partir de terça, caímos no domingo
        self.assertEqual(str(weekday), 'Sun')

    def test_extreme_values(self):
        """Testa grandes saltos temporais para garantir a matemática do módulo (%)"""
        weekday = Weeker('Fri')
        weekday.add_days(700) # Exatamente 100 semanas
        self.assertEqual(str(weekday), 'Fri')

if __name__ == '__main__':
    unittest.main()
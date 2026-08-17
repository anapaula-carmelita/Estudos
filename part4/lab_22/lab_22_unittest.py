import calendar
import unittest
from lab_22_countweekday import count_weekday_in_year

class TestCountWeekdayInYear(unittest.TestCase):

    def test_normal_year_monday(self):
        """
        Testa a ocorrência de Segundas-feiras (0) no ano de 2019.
        Espera-se o resultado de 52 semanas.
        """
        resultado = count_weekday_in_year(2019, 0)
        self.assertEqual(resultado, 52, "O ano de 2019 deve ter 52 segundas-feiras.")

    def test_leap_year_sunday(self):
        """
        Testa a ocorrência de Domingos (6) no ano 2000 (ano bissexto).
        Espera-se o resultado de 53 domingos.
        """
        resultado = count_weekday_in_year(2000, 6)
        self.assertEqual(resultado, 53, "O ano de 2000 deve ter 53 domingos.")
        
    def test_another_leap_year_tuesday(self):
        """
        Testa a ocorrência de Terças-feiras (1) no ano 2024 (ano bissexto).
        Espera-se o resultado de 53 terças-feiras.
        """
        resultado = count_weekday_in_year(2024, 1)
        self.assertEqual(resultado, 53, "O ano de 2024 deve ter 53 terças-feiras.")

if __name__ == "__main__":
    unittest.main()
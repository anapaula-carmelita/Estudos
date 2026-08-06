import unittest
import io
from unittest.mock import patch
from datetime import datetime
from lab_20_datetimeandtime import format_date

class TestFormatDatetime(unittest.TestCase):

    # O decorator intercepta os "prints" e joga na variável mock_stdout
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_format_saida_esperada(self, mock_stdout):
        # 1. EXECUÇÃO: Chamamos a função com a data de teste do laboratório
        format_date(2020, 11, 4, 14, 53, 0)
        
        # 2. CAPTURA: Pegamos tudo o que a função imprimiu
        saida = mock_stdout.getvalue()
        
        # 3. VALIDAÇÃO: Verificamos se cada linha esperada está contida na saída impressa
        self.assertIn("2020/11/04 14:53:00", saida)
        self.assertIn("20/November/04 14:53:00 PM", saida)
        self.assertIn("Wed, 2020 Nov 04", saida)
        self.assertIn("Wednesday, 2020 November 04", saida)
        self.assertIn("Weekday: 3", saida)
        self.assertIn("Day of the year: 309", saida)
        self.assertIn("Week number of the year: 44", saida)

if __name__ == '__main__':
    unittest.main()
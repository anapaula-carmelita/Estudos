import unittest
from unittest.mock import patch
from io import StringIO

# Importe a função do seu arquivo da solução
from lab_21_readints import readint

class TestReadIntSafely(unittest.TestCase):

    # 1. Caso de sucesso de primeira
    @patch('builtins.input', side_effect=['1'])
    def test_valid_input_first_try(self, mock_input):
        result = readint("Enter a number from -10 to 10: ", -10, 10)
        self.assertEqual(result, 1)

    # 2. Entrada inválida (texto) seguida por um número válido
    @patch('builtins.input', side_effect=['asd', '1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_text_then_valid(self, mock_stdout, mock_input):
        result = readint("Enter a number from -10 to 10: ", -10, 10)
        
        # Verifica se o valor final retornado está correto
        self.assertEqual(result, 1)
        # Verifica se a mensagem de erro esperada foi impressa
        self.assertIn("Error: wrong input", mock_stdout.getvalue())

    # 3. Número fora do intervalo seguido por um número válido
    @patch('builtins.input', side_effect=['100', '1'])
    @patch('sys.stdout', new_stdout=StringIO())
    @patch('sys.stdout', new_callable=StringIO)
    def test_out_of_range_then_valid(self, mock_stdout, mock_input):
        result = readint("Enter a number from -10 to 10: ", -10, 10)
        
        self.assertEqual(result, 1)
        self.assertIn("Error: the value is not within permitted range (-10..10)", mock_stdout.getvalue())

    # 4. Múltiplos erros encadeados antes de acertar
    @patch('builtins.input', side_effect=['abc', '-15', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_errors_before_valid(self, mock_stdout, mock_input):
        result = readint("Enter a number from -10 to 10: ", -10, 10)
        
        output = mock_stdout.getvalue()
        self.assertEqual(result, 5)
        self.assertIn("Error: wrong input", output)
        self.assertIn("Error: the value is not within permitted range (-10..10)", output)


if __name__ == '__main__':
    unittest.main()
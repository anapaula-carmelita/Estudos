import unittest
from unittest.mock import patch, mock_open
import sys
import io

from lab_18_evalstudents import evalstudents


class TestEvalStudents(unittest.TestCase):

    # Teste 1: Caminho Feliz (Dados perfeitos, incluindo um aluno repetido para testar a soma)
    @patch('builtins.input', return_value='notas.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='John Smith 5\nAnna Boleyn 4.5\nJohn Smith 2\n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sucesso(self, mock_stdout, mock_file, mock_input):
        evalstudents()
        output = mock_stdout.getvalue()
        
        # Anna deve ter 4.5 e John deve ter 7.0 (5 + 2)
        self.assertIn('Anna Boleyn\t4.5', output)
        self.assertIn('John Smith\t7.0', output)

    # Teste 2: Arquivo vazio
    @patch('builtins.input', return_value='vazio.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_arquivo_vazio(self, mock_stdout, mock_file, mock_input):
        evalstudents()
        output = mock_stdout.getvalue()
        
        # Verifica se caiu na exceção FileEmpty
        self.assertIn('FileEmpty: File is empty', output)

    # Teste 3: Linha ruim (Faltando dados - ex: só o nome sem a nota)
    @patch('builtins.input', return_value='ruim.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='John Smith 5\nAnna\n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_line_faltando_dados(self, mock_stdout, mock_file, mock_input):
        evalstudents()
        output = mock_stdout.getvalue()
        
        # Verifica se o programa travou corretamente acusando BadLine
        self.assertIn('BadLine:', output)

    # Teste 4: Linha ruim (Nota não é um número válido)
    @patch('builtins.input', return_value='erro_nota.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='John Smith Ausente\n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_line_nota_invalida(self, mock_stdout, mock_file, mock_input):
        evalstudents()
        output = mock_stdout.getvalue()
        
        # O ValueError deve ter sido capturado e transformado em BadLine
        self.assertIn('BadLine:', output)
        
    # Teste 5: Linha ruim (Muitos dados - ex: Nome do meio)
    @patch('builtins.input', return_value='erro_tamanho.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='John Robert Smith 5.0\n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_bad_line_muitos_dados(self, mock_stdout, mock_file, mock_input):
        evalstudents()
        output = mock_stdout.getvalue()
        
        self.assertIn('BadLine:', output)

    # Teste 6: Arquivo não encontrado
    @patch('builtins.input', return_value='fantasma.txt')
    @patch('builtins.open')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_arquivo_nao_encontrado(self, mock_stdout, mock_file, mock_input):
        # Simula o erro do sistema operacional
        mock_file.side_effect = FileNotFoundError("Arquivo sumiu")
        
        evalstudents()
        output = mock_stdout.getvalue()
        
        self.assertIn('FileNotFoundError', output)

if __name__ == '__main__':
    unittest.main()
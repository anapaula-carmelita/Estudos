import unittest
from unittest.mock import patch, mock_open
import io

# Importa a função que criamos no arquivo principal
from lab_16_histogram import histogram

class TestHistogram(unittest.TestCase):

    # Teste 1: Arquivo com letras maiúsculas, minúsculas e espaços
    @patch('builtins.input', return_value='arquivo_teste.txt')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gerar_histograma_sucesso(self, mock_stdout, mock_input):
        # Simula o conteúdo do arquivo
        conteudo_simulado = "aBc a\n"
        
        # Faz o mock do open() para retornar o nosso conteúdo simulado em vez de ler o disco
        with patch('builtins.open', mock_open(read_data=conteudo_simulado)):
            histogram()
        
        # Pega o que foi "impresso" no console pelo print()
        saida_console = mock_stdout.getvalue()
        
        # Verifica se o output esperado está no console
        expected_output = "a->2\nb->1\nc->1\n"
        self.assertEqual(saida_console, expected_output)

    # Teste 2: Arquivo não encontrado
    @patch('builtins.input', return_value='arquivo_inexistente.txt')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gerar_histograma_arquivo_nao_encontrado(self, mock_stdout, mock_input):
        # Simula o erro de arquivo não encontrado
        with patch('builtins.open', side_effect=FileNotFoundError(2, 'No such file or directory')):
            histogram()
            
        saida_console = mock_stdout.getvalue()
        
        # Verifica se a exceção foi tratada e printada corretamente
        self.assertIn('FileNotFoundError', saida_console)

if __name__ == '__main__':
    unittest.main()
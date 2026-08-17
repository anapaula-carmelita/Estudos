import unittest
from unittest.mock import patch, mock_open, call
import sys
import io

from lab_17_histogram_sorted import histogram

class TestHistogram(unittest.TestCase):

    # Teste 1: Caminho Feliz (Lendo de um arquivo e escrevendo no .hist)
    @patch('builtins.input', return_value='arquivo_teste.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='Ola Mundo! 123 @')
    def test_histograma_sucesso(self, mock_file, mock_input):
        histogram()
        
        # 1. Verifica se abriu os dois arquivos corretamente (leitura e escrita)
        mock_file.assert_any_call('arquivo_teste.txt', 'rt', encoding='utf-8')
        mock_file.assert_any_call('arquivo_teste.txt.hist', 'w', encoding='utf-8')
        
        # 2. Pega o "arquivo falso" que o nosso mock usou
        handle = mock_file()
        
        # 3. Pega uma lista de tudo que foi escrito usando a função ".write()"
        escritas = [chamada.args[0] for chamada in handle.write.call_args_list]
        
        # 4. Verifica se os valores corretos foram para o arquivo .hist (com a quebra de linha \n)
        self.assertIn('o->2\n', escritas)
        self.assertIn('l->1\n', escritas)
        self.assertIn('m->1\n', escritas)
        
        # Garante que números e símbolos foram ignorados
        self.assertNotIn('1->1\n', escritas)
        self.assertNotIn('@->1\n', escritas)

    # Teste 2: Arquivo original não encontrado
    @patch('builtins.input', return_value='arquivo_fantasma.txt')
    @patch('builtins.open')
    @patch('sys.stdout', new_callable=io.StringIO) 
    def test_histograma_arquivo_nao_encontrado(self, mock_stdout, mock_file, mock_input):
        # Força o 'open' a dar erro de cara
        mock_file.side_effect = FileNotFoundError("Arquivo inexistente")
        
        histogram()
        
        output = mock_stdout.getvalue()
        # Verifica se o programa lidou com o erro e printou FileNotFoundError
        self.assertIn('FileNotFoundError', output)
        
        # Como o primeiro 'open' (de leitura) deu erro, ele não deve ter tentado
        # fazer o segundo 'open' (de escrita do .hist). Logo, o open só foi chamado 1 vez!
        self.assertEqual(mock_file.call_count, 1)

    # Teste 3: Arquivo original existe, mas está vazio
    @patch('builtins.input', return_value='vazio.txt')
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_histograma_arquivo_vazio(self, mock_file, mock_input):
        histogram()
        
        # Verifica se abriu os dois arquivos
        mock_file.assert_any_call('vazio.txt', 'rt', encoding='utf-8')
        mock_file.assert_any_call('vazio.txt.hist', 'w', encoding='utf-8')
        
        handle = mock_file()
        
        # Como o arquivo estava vazio, o laço "for" na lista ordenada não deve rodar,
        # ou seja, a função write NÃO pode ter sido chamada nenhuma vez!
        handle.write.assert_not_called()

if __name__ == '__main__':
    unittest.main()
import os
import unittest
import tempfile
import io
from unittest.mock import patch
from lab_19_finddir import finddir

class TestFindDir(unittest.TestCase):

    def setUp(self):
        # 1. SETUP: Criamos um diretório temporário para ser nosso ambiente de teste
        self.test_dir = tempfile.TemporaryDirectory()
        self.base_path = self.test_dir.name
        
        # Vamos recriar a estrutura do laboratório do EDUBE dentro da pasta temporária:
        # tree/python
        # tree/cpp/other_courses/python
        # tree/c/other_courses/python
        
        paths_to_create = [
            os.path.join(self.base_path, 'tree', 'python'),
            os.path.join(self.base_path, 'tree', 'cpp', 'other_courses', 'python'),
            os.path.join(self.base_path, 'tree', 'c', 'other_courses', 'python')
        ]
        
        for p in paths_to_create:
            os.makedirs(p)

    def tearDown(self):
        # 3. TEARDOWN: Limpamos o ambiente (o tempfile já faz isso, mas é uma boa prática)
        self.test_dir.cleanup()

    # O decorator @patch redireciona tudo que for "impresso" (sys.stdout) para a variável mock_stdout
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_finddir_encontra_pastas(self, mock_stdout):
        # 2. EXECUÇÃO: Chamamos a função passando o diretório temporário
        finddir(self.base_path, 'python')
        
        # Pegamos tudo o que a função "printou"
        saida_impressa = mock_stdout.getvalue()
        
        # 4. VALIDAÇÃO (ASSERT): Verificamos se os caminhos absolutos estão na saída
        caminho_esperado_1 = os.path.abspath(os.path.join(self.base_path, 'tree', 'python'))
        caminho_esperado_2 = os.path.abspath(os.path.join(self.base_path, 'tree', 'cpp', 'other_courses', 'python'))
        caminho_esperado_3 = os.path.abspath(os.path.join(self.base_path, 'tree', 'c', 'other_courses', 'python'))
        
        self.assertIn(caminho_esperado_1, saida_impressa, "Deveria ter encontrado a pasta tree/python")
        self.assertIn(caminho_esperado_2, saida_impressa, "Deveria ter encontrado a pasta tree/cpp/other_courses/python")
        self.assertIn(caminho_esperado_3, saida_impressa, "Deveria ter encontrado a pasta tree/c/other_courses/python")

if __name__ == '__main__':
    unittest.main()
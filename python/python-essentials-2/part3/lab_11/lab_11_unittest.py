import unittest

from lab_11_queue import Queue
from lab_11_queue import QueueError

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        """Cria uma fila nova e vazia antes de cada teste rodar."""
        self.que = Queue()

    def test_put_and_get_success(self):
        """Testa o comportamento normal da fila (FIFO - First In, First Out)"""
        self.que.put(1)
        self.que.put("dog")
        self.que.put(False)
        
        # Como é uma fila, o primeiro a entrar (1) deve ser o primeiro a sair
        self.assertEqual(self.que.get(), 1)
        self.assertEqual(self.que.get(), "dog")
        self.assertEqual(self.que.get(), False)

    def test_get_on_empty_queue_raises_error(self):
        """Testa SE a exceção QueueError é levantada ao tentar tirar de uma fila vazia"""
        
        # O 'with self.assertRaises' cria um contexto. 
        # O teste só passa se a linha de dentro dele disparar a exceção informada.
        with self.assertRaises(QueueError):
            self.que.get()

    def test_get_raises_error_after_emptying(self):
        """Testa se a exceção funciona mesmo após a fila ter sido usada e esvaziada"""
        self.que.put("Python")
        self.que.get() # Removeu o único item, a fila ficou vazia de novo
        
        # Tentar fazer get() agora tem que estourar o QueueError
        with self.assertRaises(QueueError):
            self.que.get()
    
    def test_isempty_queue(self):
        """Testa se a a fila está vazia"""
        self.que.put("Python")
        self.que.get() # Removeu um item, a fila está vazia
        
        # Invocar a função para verificar se a fila não está vazia
        self.assertEqual(self.que.isempty(), True)
    
    def test_isnotempty_queue(self):
        """Testa se a a fila não está vazia"""
        self.que.put("Python")
        self.que.put(1)
        self.que.put("dog")
        self.que.put(False)
        self.que.get() # Removeu um item, a fila não está vazia
        self.que.get() # Removeu um item, a fila ainda não está vazia
        # Invocar a função para verificar se a fila está vazia

        self.assertEqual(self.que.isempty(), False)
if __name__ == '__main__':
    unittest.main()
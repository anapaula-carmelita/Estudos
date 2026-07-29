import unittest

from lab_09_stack import CountingStack

class TestCountingStack(unittest.TestCase):
    
    def setUp(self):
        """Este método é executado ANTES de cada teste. 
        Ele garante que teremos uma pilha zerada toda vez."""
        self.stack = CountingStack()

    def test_initial_counter_is_zero(self):
        """Testa se o contador começa em 0 ao instanciar a classe"""
        self.assertEqual(self.stack.get_counter(), 0)

    def test_push_and_pop_behavior(self):
        """Testa se o comportamento básico de Pilha (LIFO) foi mantido"""
        self.stack.push(10)
        self.stack.push(20)
        
        # O último a entrar (20) deve ser o primeiro a sair
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)

    def test_counter_increments_correctly(self):
        """Testa se o contador soma corretamente a quantidade de pops"""
        # Adiciona 5 elementos (0, 1, 2, 3, 4)
        for i in range(5):
            self.stack.push(i)
            
        # Faz pop de 3 elementos
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        
        # O contador de pops deve ser exatamente 3
        self.assertEqual(self.stack.get_counter(), 3)
        
    def test_edube_loop_scenario(self):
        """Testa exatamente o cenário exigido pelo laboratório do curso PCAP"""
        for i in range(100):
            self.stack.push(i)
            self.stack.pop()
            
        self.assertEqual(self.stack.get_counter(), 100)

if __name__ == '__main__':
    unittest.main()
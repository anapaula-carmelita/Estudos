import unittest

import os.path("/python/python-essentials-2/source-code/")

class TestMySplit(unittest.TestCase):

    def test_standard_sentence(self):
        # GIVEN (Dado que a função recebe esta string)
        input_string = "To be or not to be, that is the question"
        
        # WHEN (Quando a função é executada)
        result = mysplit(input_string)
        
        # THEN (Então ela deve retornar esta lista)
        expected_output = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
        
        # O assert do teste verifica se o resultado bate com a expectativa
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
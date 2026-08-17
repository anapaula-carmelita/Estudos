import unittest

from lab_03_caesar_cipher import caesarcipher
class TestCaesarCipher(unittest.TestCase):

    def test_caesarcipher(self):
        test_cases = [
            (
                ('abcxyzABCxyz 123', 2),
                'cdezabCDEzab 123'
            ),
            (
                ('The die is cast', 25),
                'Sgd chd hr bzrs'
            )]
        
        for (text, shift), expected in test_cases:
            with self.subTest(text=text, shift=shift):
                self.assertEqual(caesarcipher(text, shift), expected)
        

if __name__ == '__main__':
    unittest.main()
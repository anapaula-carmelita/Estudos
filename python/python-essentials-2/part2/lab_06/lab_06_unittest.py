import unittest

from lab_06_digitlife import calculatedigit
class TestDigitOfLife(unittest.TestCase):

    def test_calculatedigit(self):
        test_cases = [
            (
                "19991229",
                6
            ),
            (
                "20000101",
                4
            )]
        
        for date, expected in test_cases:
            with self.subTest(date):
                self.assertEqual(calculatedigit(date), expected)
        

if __name__ == '__main__':
    unittest.main()
import unittest

from lab_01_myownsplit import mysplit
class TestMySplit(unittest.TestCase):

    def test_mysplit(self):
        test_cases = [
            (
                "To be or not to be, that is the question",
                ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
            ),
            (
                "To    be or not to be,that is the question",
                ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
            ),
            (
                " abc ",['abc']
            ),
            (
                "Most Sacred Heart of Jesus, I      trust in You.", ["Most", "Sacred", "Heart", "of", "Jesus,", "I", "trust", "in", "You."]
            )]
        
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(mysplit(text), expected)
        

if __name__ == '__main__':
    unittest.main()
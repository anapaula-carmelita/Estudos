import unittest

from lab_07_findword import findword
class TestFindWord(unittest.TestCase):

    def test_findword(self):
        test_cases = [
            (
                ("donor", "Nabucodonosor"),
                "Yes"
            ),
            (
                ("donut", "Nabucodonosor"),
                "No"
            ),
            (
                ("dog", "vcxzxduybfdsobywuefgas"),
                "Yes"
            )]
        
        for (word, text), expected in test_cases:
            with self.subTest(word=word, text=text):
                self.assertEqual(findword(word, text), expected)
        

if __name__ == '__main__':
    unittest.main()
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
        
        for (text1, text2), expected in test_cases:
            with self.subTest(text1=text1, text2=text2):
                self.assertEqual(findword(word, text), expected)
        

if __name__ == '__main__':
    unittest.main()
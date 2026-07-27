import unittest

from lab_05_anagrams import isanagram
class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        test_cases = [
            (
                ("Listen", "Silent"),
                "Anagrams"
            ),
            (
                ("modern", "norman"),
                "Not anagrams"
            )]
        
        for (text1, text2), expected in test_cases:
            with self.subTest(text1=text1, text2=text2):
                self.assertEqual(isanagram(text1, text2), expected)
        

if __name__ == '__main__':
    unittest.main()
    
import unittest

from lab_04_palindromes import ispalindrome
class TestPalindromes(unittest.TestCase):

    def test_palindromes(self):
        test_cases = [
            (
                "Ten animals I slam in a net",
                "It's a palindrome"
            ),
            (
                "Eleven animals I slam in a net",
                "It's not a palindrome"
            )]
        
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(ispalindrome(text), expected)
        

if __name__ == '__main__':
    unittest.main()
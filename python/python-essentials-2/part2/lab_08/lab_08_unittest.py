import unittest

from lab_08_sudoku import isvalidsudoku
class TestSudoku(unittest.TestCase):

    def test_sudoku(self):
        test_cases = [
            (
"""295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672""",
                "Yes"
            ),
            (
"""195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671""",
                "No"
            )]
        
        for play, expected in test_cases:
            with self.subTest(play=play):
                self.assertEqual(isvalidsudoku(play), expected)
        

if __name__ == '__main__':
    unittest.main()
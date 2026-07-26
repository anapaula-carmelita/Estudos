import unittest

from lab_02_led_display import leddisplay
class TestLEDDisplay(unittest.TestCase):

    def test_myleddisplay(self):
        test_cases = [
            (
                "123",
"""  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 
"""
            ),
            (
                "9081726354",
"""### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 
"""
            ),
            (
                "01", 
"""###   # 
# #   # 
# #   # 
# #   # 
###   # 
"""
            )]
        
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(leddisplay(text), expected)
        

if __name__ == '__main__':
    unittest.main()
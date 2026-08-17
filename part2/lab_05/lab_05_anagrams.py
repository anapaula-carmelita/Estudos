#  File name: lab_05_anagrams.py
#  Description: A possible solution for the 'LAB Anagrams' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-27
#  Version: 1.0
#  License: Apache
#

def isanagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    for c1 in text1:
        if c1 not in text2:
            return 'Not anagrams'
    return 'Anagrams'

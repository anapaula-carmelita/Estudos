#  File name: lab_05_anagrams.py
#  Description: A possible solution for the 'LAB Find a word' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def findword(word, text):
    i = 0
    for c in word:
        i = text.find(c, i)
        if i == -1:
            return 'No'
    return 'Yes'
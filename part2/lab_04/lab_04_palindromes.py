#  File name: lab_03_caesar_cipher.py
#  Description: A possible solution for the 'LAB Palindromes' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def ispalindrome(text):
    if text == '':
        return "It's not a palindrome"
    text = text.upper().replace(' ','')
    i = 0
    n = len(text)
    while (i < n // 2):
        if text[i] != text[n - i - 1]:
            return "It's not a palindrome"
        i += 1
    return "It's a palindrome"
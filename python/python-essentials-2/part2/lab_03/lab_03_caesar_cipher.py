#  File name: lab_03_caesar_cipher.py
#  Description: A possible solution for the 'LAB Improving the Caesar Cipher' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def caesarcipher(text, vshift):
    news = ''
    for c in text:
        nc = c
        if c >= 'a' and c <= 'z':
            nc = chr(ord(c) + vshift)
            if nc > 'z':
                nc = chr(ord('a') + ord(nc) - ord('z') - 1)
        elif c >= 'A' and c <= 'Z':
            nc = chr(ord(c) + vshift)
            if nc > 'Z':
                nc = chr(ord('A') + ord(nc) - ord('Z') - 1)
        news += nc
    return news
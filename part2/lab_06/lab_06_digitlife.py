#  File name: lab_05_anagrams.py
#  Description: A possible solution for the 'LAB Digit Of Life' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def calculatedigit(strg):
    sum = 0
    while 1:
        sum = 0
        for c in strg:
            sum += int(c)
        if sum > 9:
            strg = str(sum)
        else: break
    return sum
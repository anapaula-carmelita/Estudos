#  File name: lab_21_readint.py
#  Description: A possible solution for the 'LAB Read ints safely' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def readint(prompt, min, max):
    nmin = int(min)
    nmax = int(max)
    
    while True:
        try:
            n = int(input(prompt))
            
            assert n >= nmin and n <= nmax

            return n
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")
        except:
            print("Error: wrong input")

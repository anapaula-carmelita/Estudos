#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    queue = []
    for c in s:
        
        if len(queue) > 0:
            # se caracter que fecha expressao enta
            # verifica se o ultimo da match e desempilha
            if c in [']', ')', '}']:
                if c == ']' and queue[-1] == '[':
                    queue = queue[:len(queue)-1]
                elif c == ')' and queue[-1] == '(':
                    queue = queue[:len(queue)-1]
                elif c == '}' and queue[-1] == '{':
                    queue = queue[:len(queue)-1]
                else:
                    # se nao deu match ja pode retornar NO
                    return 'NO'
            else:
                queue += [c]
        else:
            queue += [c]
    # se a pilha terminou nao vazia, nao deu match em todos
    if len(queue) > 0:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

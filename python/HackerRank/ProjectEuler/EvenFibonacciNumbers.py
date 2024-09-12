#
#  Nome do arquivo: EvenFibonacciNumbers.py
#  Descrição: Programa de uma possível solução do problema para encontrar números pares da sequência de Fibonacci de F(0) até F(N)
#  Autor: Ana Paula da Silva Souza
#  Data: 09/2024
#  Versão: 1.0
#  Licença: Apache
#

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    fib = [1, 2]
        
    f = fib[0] + fib[1]
    sum_evens = 2

    while (f < n):
        if f % 2 == 0 and f < n:
            sum_evens += f
        
        fib[0] = fib[1]
        fib[1] = f
        f = fib[0] + fib[1]

    print(sum_evens)
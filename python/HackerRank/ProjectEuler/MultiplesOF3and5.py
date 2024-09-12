#
#  Nome do arquivo: EvenFibonacciNumbers.c
#  Descrição: Programa de uma possível solução do problema para encontrar a soma dos múltimos de 3 e 5 menores que N
#  Autor: Ana Paula da Silva Souza
#  Data: 09/2024
#  Versão: 1.0
#  Licença: Apache
#

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    
    
    m3 = (n - 1)//3
    m5 = (n - 1)//5
    m15 = (n - 1)//15
    s = (3*m3*(m3+1)//2) + (5*m5*(m5+1)//2) - (15*m15 *(m15+1)//2)
    
    print(s)

#!/bin/python3

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
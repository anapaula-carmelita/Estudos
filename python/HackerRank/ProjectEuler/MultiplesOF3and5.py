#!/bin/python3


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    
    
    m3 = (n - 1)//3
    m5 = (n - 1)//5
    m15 = (n - 1)//15
    s = (3*m3*(m3+1)//2) + (5*m5*(m5+1)//2) - (15*m15 *(m15+1)//2)
    
    print(s)

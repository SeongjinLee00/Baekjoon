from math import gcd

def solution(a, b):

    g=gcd(a,b)
    b//=g
    
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    
    if b==1:
        return 1
    else:
        return 2
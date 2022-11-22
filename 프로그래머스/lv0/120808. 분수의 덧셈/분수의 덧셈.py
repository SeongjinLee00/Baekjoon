from math import gcd

def solution(denum1, num1, denum2, num2):
    N=gcd(num1,num2)
    
    N*=((num1//N)*(num2//N))
    
    D=denum1*(N//num1)+denum2*(N//num2)
    
    d=gcd(D,N)
    D//=d
    N//=d
    return [D,N]
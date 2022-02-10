def gcd(num1,num2): # Euclidian 
    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    r=a%b
    if a%b==0:
        return b
    else:
        return gcd(b,r)
def lcm(num1,num2):
    return num1*num2//gcd(num1,num2)
#####################################################################################
#####################################################################################
import math

A, B=map(int,input().split())

a=int(math.sqrt(A*B))+1

while True:
    if (A*B)%a==0:
        b=(A*B)//a
        if gcd(a,b)==A:
            print(a, b)
            break
        else:
            a=a-1
    else:
        a=a-1
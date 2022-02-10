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
n=int(input())

D=n//2
N=n-D

while True:
    if gcd(D,N)==1:
        break
    else:
        D=D-1
        N=N+1

print(D, N)
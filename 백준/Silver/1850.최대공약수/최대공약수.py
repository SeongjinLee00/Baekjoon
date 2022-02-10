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

A,B=map(int,input().split())
C=gcd(A,B)
print('1'*C)
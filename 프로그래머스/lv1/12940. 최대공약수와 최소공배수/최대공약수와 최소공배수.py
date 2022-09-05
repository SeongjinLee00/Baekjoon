def gcd(num1,num2): # Euclidian 

    a=max(num1,num2)
    b=min(num1,num2)

    r=a%b

    if a%b==0:
        return b
    else:
        return gcd(b,r)

def solution(n, m):
    return [gcd(n,m),n*m//gcd(n,m)]
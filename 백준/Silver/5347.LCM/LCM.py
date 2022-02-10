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

for _ in range(n):
    a,b=map(int,input().split())

    print(a*b//gcd(a,b))
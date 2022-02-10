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
N=int(input())

R, *numbers=map(int,input().split())

for number in numbers:

    print(f'{R//gcd(R,number)}/{number//gcd(R,number)}')
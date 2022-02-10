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


N1, D1= map(int,input().split())
N2, D2= map(int,input().split())

D3=(D1*D2)//gcd(D1,D2)
N3=N1*(D3//D1)+N2*(D3//D2)

d=gcd(N3,D3)
D3=D3//d
N3=N3//d

print(N3, D3)
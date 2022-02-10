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

A, B=map(int,input().split())

print(gcd(A,B))
print(A*B//gcd(A,B))
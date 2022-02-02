N,K=map(int,input().split())

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

up=1
for i in range(K):
    up=up*(N-i)

print(up//factorial(K))
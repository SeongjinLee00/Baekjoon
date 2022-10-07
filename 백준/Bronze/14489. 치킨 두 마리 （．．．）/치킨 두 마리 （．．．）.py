a,b=map(int,input().split())
c=int(input())
balance=a+b

if balance>=2*c:
    print(balance-2*c)
else:
    print(balance)
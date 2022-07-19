numbers=list(map(int,input().split()))

a=numbers.count(1)
b=numbers.count(2)

if a>b:
    print(1)
else:
    print(2)
L,P=map(int,input().split())

p=L*P

numbers=list(map(int,input().split()))

for number in numbers:
    print(number-p,end=" ")
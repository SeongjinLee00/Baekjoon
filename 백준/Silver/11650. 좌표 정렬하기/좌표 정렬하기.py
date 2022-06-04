numbers=[]

N=int(input())

for _ in range(N):
    x,y=map(int,input().split())
    numbers.append([x,y])

numbers.sort()

for x,y in numbers:
    print(x,y)
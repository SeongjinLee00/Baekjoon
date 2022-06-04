N=int(input())

numbers=[]

for _ in range(N):
    x,y=map(int,input().split())
    numbers.append([x,y])

numbers.sort(key=lambda x:(x[1],x[0]))

for x,y in numbers:
    print(x,y)
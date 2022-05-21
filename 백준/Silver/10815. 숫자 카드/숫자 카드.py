N=int(input())
numbers=set(map(int,input().split()))
M=int(input())
numbers2=list(map(int,input().split()))

for n in numbers2:
    if n in numbers:
        print("1", end=" ")
    else:
        print("0", end=" ")
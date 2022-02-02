N=int(input())
list1=set(map(int,input().split()))

M=int(input())
list2=list(map(int,input().split()))

for number in list2:
    if number in list1:
        print(1)
    else:
        print(0)
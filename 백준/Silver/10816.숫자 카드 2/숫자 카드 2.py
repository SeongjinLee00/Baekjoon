import bisect

N=int(input())

cards=list(map(int,input().split()))
cards.sort()
M=int(input())

numbers=list(map(int,input().split()))

for n in numbers:
    left=bisect.bisect_left(cards,n)
    right=bisect.bisect_right(cards,n)
    print(right-left,end=' ')
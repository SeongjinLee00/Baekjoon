from itertools import combinations

N,L,R,X=map(int,input().split())

numbers=list(map(int,input().split()))

numbers.sort()

if N==1:
    print(0)
    exit(0)

cnt=0
for k in range(2,16):
    comb=combinations(numbers,k)

    for c in comb:
        if c[-1]-c[0]>=X and L<=sum(c)<=R:
            cnt+=1

print(cnt)
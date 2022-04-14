from itertools import combinations

N,M=map(int,input().split())

members=[[0]]
idx=[i for i in range(1,M+1)]

for _ in range(M):
    a,*b=map(int,input().split())
    members.append(list(b))

flag=0
for k in range(1,M+1):
    comb=combinations(idx,k)
    for c in comb:
        possible=[]
        for person in c:
            possible+=members[person]
        tmp=0
        for i in range(1,N+1):
            if i in possible:
                tmp+=1
        if tmp==N:
            print(k)
            exit(0)

print(-1)
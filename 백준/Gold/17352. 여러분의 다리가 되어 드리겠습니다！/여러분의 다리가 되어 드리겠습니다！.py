N=int(input())

parents=[i for i in range(N)]

def union(x,y):
    a=find(x)
    b=find(y)

    parents[max(a,b)]=min(a,b)

def find(x):

    if x!=parents[x]:
        parents[x]=find(parents[x])
    
    return parents[x]

for _ in range(N-2):
    a,b=map(int,input().split())

    union(a-1,b-1)

for i in range(N):
    find(i)

for i in range(N-1):
    if parents[i]!=parents[i+1]:
        print(i+1,i+2)
        exit(0)
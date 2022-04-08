import sys

def union(x,y):
    a=find(x)
    b=find(y)

    minab=min(a,b)
    maxab=max(a,b)

    if a!=b:
        length[minab]+=length[maxab]
    print(length[minab])
    parent[maxab]=minab

    
def find(x):

    if x!=parent[x]:
        parent[x]=find(parent[x])

    return parent[x]


T=int(input())

for _ in range(T):
    parent=[i for i in range(200001)]
    length=[1]*200001
    number={}
    M=int(input())

    my_number=1
    for _ in range(M):
        a,b=sys.stdin.readline().split()

        if a in number:
            x=number[a]
        else:
            x=my_number
            number[a]=x
            my_number+=1
        
        if b in number:
            y=number[b]
        else:
            y=my_number
            number[b]=y
            my_number+=1
    
        union(x,y)
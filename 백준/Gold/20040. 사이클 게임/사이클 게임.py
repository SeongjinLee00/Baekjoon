n,m=map(int,input().split())

parent=[i for i in range(n)]

def union(x,y):
    parent[find(y)]=find(x)

def find(x):
    tmp = [x]
    while x != parent[x]:
        x = parent[x]
        tmp.append(x)
    for n in tmp:
        parent[n] = x
    return x

for turn in range(1,m+1):
    a,b=map(int,input().split())

    if find(a)==find(b):
        print(turn)
        exit(0)
    else:
        union(a,b)

print(0)
N=int(input())

parent=[i for i in range(N+1)]

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

M=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            union(i+1,j+1)

numbers=list(map(int,input().split()))

tmp=find(numbers[0])
for n in numbers:
    if tmp!=find(n):
        print('NO')
        exit(0)

print('YES')
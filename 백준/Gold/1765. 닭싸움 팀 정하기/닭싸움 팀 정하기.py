n=int(input())
m=int(input())

parents=[i for i in range(n)]

def union(x,y):
    a=find(x)
    b=find(y)

    parents[max(a,b)]=min(a,b)

def find(x):

    if parents[x]!=x:
        parents[x]=find(parents[x])
    
    return parents[x]

enemies=[[] for _ in range(n)]

for _ in range(m):
    s,a,b=input().split()
    a=int(a)
    b=int(b)
    if s=='F':
        union(a-1,b-1)
    else:
        enemies[a-1].append(b-1)
        enemies[b-1].append(a-1)

for i in range(len(enemies)):
    for enemy in enemies[i]:
        for enemyofenemy in enemies[enemy]:
            union(enemyofenemy,i)

for i in range(n):
    find(i)

print(len(set(parents)))
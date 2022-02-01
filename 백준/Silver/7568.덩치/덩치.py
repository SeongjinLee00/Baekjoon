N=int(input())

list1=[]
list2=[]
A=[]
rank=[1 for i in range(N)]
for i in range(N):
    list1.append(list(map(int,input().split())))

for j in range(N):
    for k in range(N):
        if (list1[j][0]<list1[k][0]) and (list1[j][1]<list1[k][1]):
            rank[j] += 1

for k in range(N):
    print(rank[k],end=' ')
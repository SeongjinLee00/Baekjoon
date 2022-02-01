N=int(input())

lst=[]
for _ in range(6):
    a,b = list(map(int,input().split()))
    lst.append([a,b])

hor=[]
ver=[]

for i in range(6):
    if lst[i][0]==3 or lst[i][0]==4:
        ver.append(lst[i][1])
    if lst[i][0]==1 or lst[i][0]==2:
        hor.append(lst[i][1])

lst=lst*2

for i in range(len(lst)):
    if lst[i][1]==max(hor):
        ver.append(lst[i+3][1])
        break

for i in range(len(lst)):
    if lst[i][1]==max(ver):
        hor.append(lst[i+3][1])
        break

print((max(hor)*max(ver)-hor[-1]*ver[-1])*N)
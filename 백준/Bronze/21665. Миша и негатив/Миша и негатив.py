r,c=map(int,input().split())

a=[]
b=[]
for _ in range(r):
    a.append(list(input()))
input()
for _ in range(r):
    b.append(list(input()))
    
ans=0

for i in range(r):
    for j in range(c):
        if a[i][j]==b[i][j]:
            ans+=1
print(ans)
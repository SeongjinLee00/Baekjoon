N,M=9,9

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))

ans=-1
ans_coord=(0,0)
for i in range(N):
    for j in range(M):
        if numbers[i][j]>ans:
            ans=numbers[i][j]
            ans_coord=(i+1,j+1)

print(ans)
print(*ans_coord)
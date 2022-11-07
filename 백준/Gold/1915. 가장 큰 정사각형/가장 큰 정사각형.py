N,M=map(int,input().split())

if N==0 and M==0:
    exit(0)

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input())))

for i in range(1,len(numbers)):
    for j in range(1,len(numbers[0])):
        if numbers[i][j]:
            numbers[i][j]=min(numbers[i-1][j-1],numbers[i-1][j],numbers[i][j-1])+1

ans=0

for i in range(len(numbers)):
    for j in range(len(numbers[0])):
        ans=max(ans,numbers[i][j])

print(ans*ans)
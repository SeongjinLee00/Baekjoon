N,K=map(int,input().split())

coins=[]
count=0
for _ in range(N):
    coins.append(int(input()))

for i in range(N-1,-1,-1):
    while K>=coins[i]:
        K-=coins[i]
        count+=1
        if K==0:
            print(count)
            exit(0)
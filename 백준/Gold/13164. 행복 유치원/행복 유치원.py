n,k=map(int,input().split())

numbers=list(map(int,input().split()))

diffs=[0]*(n-1)

for i in range(n-1):
    diffs[i]=numbers[i+1]-numbers[i]

diffs.sort()

print(sum(diffs[:(n-k)]))
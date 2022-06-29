from collections import defaultdict

N,M=map(int,input().split())

numbers=list(map(int,input().split()))

for i in range(N-1):
    numbers[i+1]+=numbers[i]

for i in range(N):
    numbers[i]%=M

cnts=defaultdict(int)

for number in numbers:
    cnts[number]+=1

ans=0
for num, cnt in cnts.items():
    ans+=cnt*(cnt-1)//2

ans+=cnts[0]

print(ans)
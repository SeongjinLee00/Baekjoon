N=int(input())

numbers=list(map(int,input().split()))

dp1=[1]*N

for i in range(N):
    for j in range(i):
        if numbers[i]>numbers[j] and dp1[j]>=dp1[i]:
            dp1[i]=dp1[j]+1

numbers.reverse()

dp2=[1]*N
for i in range(N):
    for j in range(i):
        if numbers[i]>numbers[j] and dp2[j]>=dp2[i]:
            dp2[i]=dp2[j]+1

dp2.reverse()
bitonic=[0]*N

for i in range(N):
    bitonic[i]=dp1[i]+dp2[i]

print(max(bitonic)-1)
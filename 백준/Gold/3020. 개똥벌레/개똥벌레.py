import sys
input=sys.stdin.readline

L,H=map(int,input().split())

delta=[0]*(H+1)

for i in range(L):
    h=int(input())
    
    if i%2==0:
        delta[0]+=1
        delta[h]-=1
    else:
        delta[-1]-=1
        delta[-1-h]+=1

for i in range(len(delta)-1):
    delta[i+1]+=delta[i]

delta.pop()

ans1=min(delta)
print(ans1, delta.count(ans1))
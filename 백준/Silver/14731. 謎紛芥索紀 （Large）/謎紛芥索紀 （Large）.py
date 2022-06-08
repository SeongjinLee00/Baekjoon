import sys

input = sys.stdin.readline

N=int(input())

MOD=1000000007
ans=0
for _ in range(N):
    C,K=map(int,input().split())

    ans+=(C*K)*pow(2,K-1,MOD)

print(ans%MOD)
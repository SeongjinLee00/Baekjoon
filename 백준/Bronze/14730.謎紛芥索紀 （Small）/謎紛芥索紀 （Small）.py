import sys

N=int(input())

sum=0
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    sum+=a*b

print(sum)
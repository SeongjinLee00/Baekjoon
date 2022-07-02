import sys

input=sys.stdin.readline

N=int(input())

ans=0

lines=[]

for _ in range(N):
    s,e=map(int,input().split())
    lines.append((s,e))

lines.sort()

ans=0
S=lines[0][0]
E=lines[0][1]
for s,e in lines:
    if S<=s and e<=E:
        continue
    elif s<=E:
        E=e
    else:
        ans+=(E-S)
        S=s
        E=e

ans+=(E-S)
print(ans)
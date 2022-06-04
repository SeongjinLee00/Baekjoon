N,M=map(int,input().split())

set_a=set()

for _ in range(N):
    set_a.add(input())
cnt=0
for _ in range(M):
    s=input()
    if s in set_a:
        cnt+=1

print(cnt)
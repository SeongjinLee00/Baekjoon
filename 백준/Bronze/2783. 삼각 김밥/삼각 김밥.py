x,y=map(int,input().split())

c=y/x

N=int(input())

for _ in range(N):
    x,y=map(int,input().split())
    c=max(c,y/x)

print(1000/c)
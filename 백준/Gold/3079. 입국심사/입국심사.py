import sys

N,M=map(int,sys.stdin.readline().split())

times=[]
for _ in range(N):
    times.append(int(sys.stdin.readline()))

# 최솟값을 구하는 문제, F F F F F F F F T T T T T T T T T 

def check(mid):
    a=0
    for i in range(len(times)):
        a+=mid//times[i]
        if a>=M:
            return True
    return False

start=0
end=10**18

while start+1<end:
    mid=(start+end)//2
    if check(mid):
        end=mid
    else:
        start=mid

print(end)
import bisect
import sys

N,C=map(int,sys.stdin.readline().split())

houses=[]
for _ in range(N):
    houses.append(int(sys.stdin.readline()))
houses.sort()

distance=(houses[-1]-houses[0])//(C-1) # 0과 distance 사이에 답이 있을것이므로, 그 사이에서 이분탐색

start=1
end=distance
d=(start+end)//2

while start<=end:
    i=houses[0]
    cnt=1
    while cnt<C and i<=houses[-1]:
        try:
            i=houses[bisect.bisect_left(houses,i+d)]
            cnt+=1
        except:
            break
    if cnt>=C:
        start=d+1
    else:
        end=d-1
    d=(start+end)//2

print(d)
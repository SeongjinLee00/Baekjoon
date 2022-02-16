N,M,L=map(int,input().split())
stations=list(map(int,input().split()))
stations=[0]+stations+[L]
stations.sort()

start=0
end=L
d=(start+end)//2
while start+1<end:
    d=(start+end)//2
    cnt=0

    for i in range(len(stations)-1): # 모든 구간을 d보다 작거나 같게 만드는 방법으로 휴게소를 지음
        cnt+=(stations[i+1]-stations[i]-1)//d

    if cnt>M:
        start=d
    else:
        end=d

print(end)

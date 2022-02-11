import itertools # 발견1, 무식하게 6중포문같은거 쓰지말고 라이브러리 쓰자

N,M=map(int,input().split())

city=[]
chickens=[]
houses=[]

for _ in range(N):
    city.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if city[i][j]==2:
            chickens.append([i, j])
        if city[i][j]==1:    
            houses.append([i,j])

sums=[]

for combination in itertools.combinations(chickens, M):
    sum=0
    for house in houses: # 각 집별로
        temp=999999
        for i in range(len(combination)): # 모든 살아남은 치킨집을 돌면서 거리를 조사함
            if (abs(house[0]-combination[i][0])+abs(house[1]-combination[i][1]))<temp:
                temp=(abs(house[0]-combination[i][0])+abs(house[1]-combination[i][1]))
        sum=sum+temp
    sums.append(sum)

if len(sums)==1: # 경우의 수가 하나인 예외적 상황
    print(sums[0])
else:
    print(min(sums))
N,M=map(int,input().split())

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))


max=0

def sibal():
    global max
    for r in range(N):
        for c in range(M):
            sum=0
            for k in range(4):
                rr=r+dr[k]
                cc=c+dc[k]
                if 0<=rr<N and 0<=cc<M:
                    sum+=numbers[rr][cc]
            if sum>max:
                max=sum

dr=[0,0,0,0]
dc=[0,1,2,3]
sibal()
dr=[0,1,2,3]
dc=[0,0,0,0]
sibal()
dr=[0,0,1,1]
dc=[0,1,0,1]
sibal()
dr=[0,1,2,2]
dc=[0,0,0,1]
sibal()
dr=[0,1,0,0]
dc=[0,0,1,2]
sibal()
dr=[0,0,1,2]
dc=[0,1,1,1]
sibal()
dr=[1,1,1,0]
dc=[0,1,2,2]
sibal()
dr=[0,1,2,2]
dc=[1,1,1,0]
sibal()
dr=[0,0,0,1]
dc=[0,1,2,2]
sibal()
dr=[0,0,1,2]
dc=[0,1,0,0]
sibal()
dr=[0,1,1,1]
dc=[0,0,1,2]
sibal()
dr=[0,1,1,2]
dc=[0,0,1,1]
sibal()
dr=[0,1,1,0]
dc=[1,0,1,2]
sibal()
dr=[0,1,1,2]
dc=[1,0,1,0]
sibal()
dr=[0,0,1,1]
dc=[0,1,1,2]
sibal()
dr=[1,1,1,0]
dc=[0,1,2,1]
sibal()
dr=[0,1,2,1]
dc=[0,0,0,1]
sibal()
dr=[0,0,0,1]
dc=[0,1,2,1]
sibal()
dr=[1,0,1,2]
dc=[0,1,1,1]
sibal()

print(max)
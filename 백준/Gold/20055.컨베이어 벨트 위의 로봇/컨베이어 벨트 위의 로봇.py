N,K=map(int,input().split())

health=list(map(int,input().split()))

robots=[]

def rotate():
    health.insert(0,health[-1])
    health.pop()

def move():
    for i in range(len(robots)):
        robots[i]=robots[i]+1
    
    if len(robots)==0:
        pass
    else:
        if robots[0]==N-1:
            robots.remove(N-1)

    for i in range(len(robots)):
        if health[robots[i]+1]!=0 and robots.count(robots[i]+1)==0:
            robots[i]=robots[i]+1
            health[robots[i]] -=1
    
    if len(robots)==0:
        pass
    else:
        if robots[0]==N-1:
            robots.remove(N-1)

def geton():
    if health[0]!=0:
        robots.append(0)
        health[0]=health[0]-1

rotate()
geton()
count=1
if health.count(0)>=K:
    print(count)
else:
    while True:
        rotate()
        move()
        geton()
        count=count+1
        if health.count(0)>=K:
            print(count)
            break
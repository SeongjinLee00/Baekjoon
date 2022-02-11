gear1=list(map(int,list(input()))) # 인덱스 0이 북쪽, 4가 남쪽 clockwise
gear2=list(map(int,list(input()))) # N극은 0 S극은 1
gear3=list(map(int,list(input())))
gear4=list(map(int,list(input())))

K=int(input())

moves=[]
def clockwise(gear):
    gear.insert(0,gear[-1])
    gear.pop()
def counter_clockwise(gear):
    gear.append(gear[0])
    gear.remove(gear[0])

def operate(gear, dir):
    if dir==1:
        clockwise(gear)
    elif dir==-1:
        counter_clockwise(gear)

for _ in range(K):
    a,b=map(int,input().split()) # b=1이면 시계, -1이면 반시계
    if a==1:
        operate(gear1,b)
        if gear1[2+b]+gear2[6]==1:
            operate(gear2,-b)
            if gear2[2-b]+gear3[6]==1:
                operate(gear3,b)
                if gear3[2+b]+gear4[6]==1:
                    operate(gear4,-b)

    if a==2:
        operate(gear2,b)
        if gear2[2+b]+gear3[6]==1:
            operate(gear3,-b)
            if gear3[2-b]+gear4[6]==1:
                operate(gear4,b)
        if gear2[6+b]+gear1[2]==1:
            operate(gear1,-b)

    if a==3:
        operate(gear3,b)
        if gear3[2+b]+gear4[6]==1:
            operate(gear4,-b)
        if gear3[6+b]+gear2[2]==1:
            operate(gear2,-b)
            if gear2[6-b]+gear1[2]==1:
                operate(gear1,b)

    if a==4:
        operate(gear4,b)
        if gear4[6+b]+gear3[2]==1:
            operate(gear3,-b)
            if gear3[6-b]+gear2[2]==1:
                operate(gear2,b)
                if gear2[6+b]+gear1[2]==1:
                    operate(gear1,-b)

score=0
if gear1[0]==1:
    score+=1
if gear2[0]==1:
    score+=2
if gear3[0]==1:
    score+=4
if gear4[0]==1:
    score+=8

print(score)
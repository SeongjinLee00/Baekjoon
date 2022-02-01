C,R=map(int,input().split())
K=int(input())
x,y=1,1

currup=R
currdown=1
currleft=1
currright=C

if K>C*R:
    print(0)
else:
    count=1
    while count !=K:
        while y!=currup and count !=K:
            y=y+1
            count += 1
        currleft += 1

        while x!=currright and count !=K:
            x=x+1
            count += 1
        currup -=1

        while y!=currdown and count !=K:
            y=y-1
            count +=1
        currright -=1

        while x!=currleft and count !=K:
            x=x-1
            count += 1
        currdown +=1

    print(x,y)
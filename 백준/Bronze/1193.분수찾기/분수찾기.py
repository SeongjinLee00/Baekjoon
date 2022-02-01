X=int(input())

if X==1:
    print('1/1')
if X==2:
    print('1/2')
if X==3:
    print('2/1')
if X==4:
    print('3/1')

count=4
up=3
down=1
if X>=5:
    while count<=X:
        while up>1:
            up=up-1
            down=down+1
            count=count+1
            if count==X:
                print(f'{up}/{down}')
        down+=1
        count=count+1
        if count==X:
            print(f'{up}/{down}')
        while down>1:
            up=up+1
            down=down-1
            count=count+1
            if count==X:
                print(f'{up}/{down}')
        up+=1
        count=count+1
        if count==X:
            print(f'{up}/{down}')
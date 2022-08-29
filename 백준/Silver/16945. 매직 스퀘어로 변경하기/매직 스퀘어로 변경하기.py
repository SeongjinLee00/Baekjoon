arr=[[0]*3 for _ in range(3)]
numbers=[]
for _ in range(3):
    numbers.append(list(map(int,input().split())))
ans=99999999
def magic_square(num,used):
    global ans
    if num==9:
        tmp=0
        for i in range(3):
            for j in range(3):
                tmp+=abs(arr[i][j]-numbers[i][j])
        ans=min(tmp,ans)        
        return

    if num==0:
        i, j = 0, 0
    elif num==1:
        i, j = 0, 1
    elif num==2:
        i, j = 0, 2
    elif num==3:
        i, j = 1, 0
    elif num==4:
        i, j = 1, 1
    elif num==5:
        i, j = 1, 2
    elif num==6:
        i, j = 2, 0
    elif num==7:
        i, j = 2, 1
    elif num==8:
        i, j = 2, 2
    
    for k in range(1,10):
        if k in used:
            continue
        arr[i][j]=k
        if num==2 and arr[0][0]+arr[0][1]+arr[0][2]!=15:
            continue
        elif num==5 and arr[1][0]+arr[1][1]+arr[1][2]!=15:
            continue
        elif num==8 and arr[2][0]+arr[2][1]+arr[2][2]!=15:
            continue
        elif num==6 and arr[0][0]+arr[1][0]+arr[2][0]!=15:
            continue
        elif num==7 and arr[0][1]+arr[1][1]+arr[2][1]!=15:
            continue
        elif num==8 and arr[0][2]+arr[1][2]+arr[2][2]!=15:
            continue
        elif num==6 and arr[0][2]+arr[1][1]+arr[2][0]!=15:
            continue
        elif num==8 and arr[0][0]+arr[1][1]+arr[2][2]!=15:
            continue
        used.add(k)
        magic_square(num+1, used)
        used.remove(k)

magic_square(0, set())
print(ans)
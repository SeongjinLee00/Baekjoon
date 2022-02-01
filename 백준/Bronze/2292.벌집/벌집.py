N=int(input())

left=2
right=8
count=1

if N==1:
    print(1)
else:
    while True:
        if N in range(left,right):
            print(count+1)
            break
        left=left+6*count
        right=right+6*(count+1)
        count=count+1
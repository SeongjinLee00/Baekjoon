N,L=map(int,input().split())

length=0
list=[]

while L<=100:
    if L%2==0:
        if N%L==L//2:
            length=L
            break
        else:
            L=L+1
    if L%2==1:
        if N%L==0:
            length=L
            break
        else:
            L=L+1

if L>100:
    print(-1)
else:
    if length%2==1:
        for i in range(-((length-1)//2),((length-1)//2)+1,1):
            list.append(N//L+i)
    elif length%2==0:
        for j in range(-(length//2-1),length//2+1):
            list.append(N//L+j)

if len(list)!=0 and list[0]<0:
    print(-1)
else:
    for number in list:
        print(number,end=' ')
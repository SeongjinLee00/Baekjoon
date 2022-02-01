X,Y=map(int,input().split())

Xdivide=[]
Ydivide=[]

N=int(input())
a=0
b=0
for _ in range(N):
    a,b=map(int,input().split())
    if a==0:
        Ydivide.append(b)
    if a==1:
        Xdivide.append(b)

Xdivide.sort()
Ydivide.sort()

if len (Xdivide)==0:
    Ylens=[Ydivide[0]]

    for i in range(len(Ydivide)-1):
        Ylens.append(Ydivide[i+1]-Ydivide[i])

    Ylens.append(Y-Ydivide[-1])

    print(X*max(Ylens))

elif len(Ydivide)==0:
    Xlens=[Xdivide[0]]

    for i in range(len(Xdivide)-1):
        Xlens.append(Xdivide[i+1]-Xdivide[i])

    Xlens.append(X-Xdivide[-1])

    print(Y*max(Xlens))    

else:

    Xlens=[Xdivide[0]]
    Ylens=[Ydivide[0]]

    for i in range(len(Xdivide)-1):
        Xlens.append(Xdivide[i+1]-Xdivide[i])

    for i in range(len(Ydivide)-1):
        Ylens.append(Ydivide[i+1]-Ydivide[i])

    Xlens.append(X-Xdivide[-1])
    Ylens.append(Y-Ydivide[-1])

    print(max(Xlens)*max(Ylens))
N,M=map(int,input().split())

numbers=list(map(int,input().split()))

i=0
if N==1:
    if numbers[0]==M:
        print(1)
        exit(0)
    else:
        print(0)
        exit(0)
j=1
cnt=0
partialsum=numbers[i]+numbers[j]

while True:
    if partialsum<M:
        j=j+1
        if j==N:
            break
        partialsum+=numbers[j]
    elif partialsum>M:
        partialsum-=numbers[i]
        i=i+1
    else:
        cnt+=1
        partialsum-=numbers[i]
        i=i+1
        j=j+1
        if j==N:
            break
        partialsum+=numbers[j]

print(cnt)
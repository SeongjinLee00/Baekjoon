N=int(input())
numbers=list(map(int,input().split()))

X=int(input())

numbers.sort()

i=0
j=N-1

cnt=0
while i<j:
    if numbers[i]+numbers[j]==X:
        cnt+=1
        i+=1
        j-=1
    elif numbers[i]+numbers[j]<X:
        i+=1
    elif numbers[i]+numbers[j]>X:
        j-=1

print(cnt)
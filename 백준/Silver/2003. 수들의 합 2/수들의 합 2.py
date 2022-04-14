N,M=map(int,input().split())

numbers=list(map(int,input().split()))

i=0
j=1
cnt=0
while j<N+1:
    if sum(numbers[i:j])<M:
        j=j+1
    elif sum(numbers[i:j])>M:
        i=i+1
    else:
        cnt+=1
        i=i+1
        j=j+1

print(cnt)
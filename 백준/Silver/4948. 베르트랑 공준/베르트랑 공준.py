numbers=[True]*250001
numbers[0]=False
numbers[1]=False

for i in range(2,250001):
    if numbers[i]:
        for j in range(2*i,250001,i):
            numbers[j]=False

while True:
    n=int(input())
    if n==0:
        exit(0)

    ans=0

    for k in range(n+1,2*n+1):
        if numbers[k]:
            ans+=1

    print(ans)
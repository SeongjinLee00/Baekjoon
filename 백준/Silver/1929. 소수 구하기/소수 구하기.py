numbers=[True]*1000001
numbers[0]=False
numbers[1]=False

for i in range(2,1000001):
    if numbers[i]:
        for j in range(2*i,1000001,i):
            numbers[j]=False

N,M=map(int,input().split())

for k in range(N,M+1):
    if numbers[k]:
        print(k)
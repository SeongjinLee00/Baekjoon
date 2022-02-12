import sys

N=int(input())

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,sys.stdin.readline().split())))

numbers.sort(key=lambda x:(x[1],x[0]))

time=0
cnt=0
for i in range(len(numbers)):
    if numbers[i][0]>=time:
        cnt+=1
        time=numbers[i][1]

print(cnt)
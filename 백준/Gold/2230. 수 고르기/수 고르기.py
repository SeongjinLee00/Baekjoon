import sys

input = sys.stdin.readline

N,M = map(int,input().split())

numbers=[]

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

i = 0
for j in range(N):
    if numbers[j]-numbers[i]>=M:
        now=numbers[j]-numbers[i]
        break
while True:
    if numbers[j]-numbers[i]>M:
        i+=1
    elif numbers[j]-numbers[i]<M:
        j+=1
    else:
        print(M)
        exit(0)
    if i==N or j==N:
        print(now)
        exit(0)
    if now>numbers[j]-numbers[i]>=M:
        now=min(now,numbers[j]-numbers[i])
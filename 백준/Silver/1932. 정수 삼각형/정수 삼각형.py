N=int(input())

numbers=[]
for _ in range(N):
    numbers.append(list(map(int,input().split())))
R=0
for R in range(1,N):
    for c in range(len(numbers[R])):
        if c==0:
            numbers[R][c]+=numbers[R-1][c]
        elif c==len(numbers[R])-1:
            numbers[R][c]+=numbers[R-1][c-1]
        else:
            numbers[R][c]+=max(numbers[R-1][c],numbers[R-1][c-1])

print(max(numbers[R]))
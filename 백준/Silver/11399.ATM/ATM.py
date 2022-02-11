N=int(input())

numbers=list(map(int,input().split()))

numbers.sort()

for i in range(1,N):
    numbers[i]=numbers[i]+numbers[i-1]

print(sum(numbers))
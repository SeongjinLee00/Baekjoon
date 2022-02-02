numbers=list(map(int,input().split()))

sum=0
for i in range(len(numbers)):
    sum += numbers[i]**2

print(sum%10)
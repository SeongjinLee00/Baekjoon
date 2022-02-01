N=int(input())
numbers=list(map(int,input().split()))

count=len(numbers)
for number in numbers:
    for n in range(2,number):
        
        if number%n==0:
            count -=1
            break
if 1 in numbers:
    count=count-1

print(count)
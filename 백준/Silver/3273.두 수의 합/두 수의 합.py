n=int(input())
numbers=list(map(int,input().split()))
x=int(input())

numbers.sort()
count=0

i=0
j=n-1

while i<j:
    if numbers[i]+numbers[j]<x:
        i=i+1
    elif numbers[i]+numbers[j]==x:
        count=count+1
        i=i+1
    elif numbers[i]+numbers[j]>x:
        j=j-1

print(count)
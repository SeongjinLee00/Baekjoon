N=int(input())
numbers=list(map(int,input().split()))

numbers.sort()
i=0
j=N-1

value=9999999999999
sol1=0
sol2=0

while i<j:
    if abs(numbers[i]+numbers[j])<value:
        value=abs(numbers[i]+numbers[j])
        sol1=numbers[i]
        sol2=numbers[j]
    
    if numbers[i]+numbers[j]<0:
        i+=1
    elif numbers[i]+numbers[j]>0:
        j-=1
    else:
        break

print(sol1, sol2)
N=int(input())
numbers=list(map(int,input().split()))

i=0
j=N-1

value=9999999999999

while i<j:
    if abs(numbers[i]+numbers[j])<abs(value):
        value=numbers[i]+numbers[j]
    
    if numbers[i]+numbers[j]<0:
        i+=1
    elif numbers[i]+numbers[j]>0:
        j-=1
    else:
        break

print(value)
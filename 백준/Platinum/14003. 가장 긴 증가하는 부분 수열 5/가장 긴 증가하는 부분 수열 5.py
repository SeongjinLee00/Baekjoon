from bisect import bisect_left

N=int(input())
numbers=list(map(int,input().split()))

stack=[numbers[0]]
index=[0]*N

for i in range(len(numbers)):
    number=numbers[i]
    if stack[-1]<number:
        stack.append(number)
        index[i]=len(stack)
    else:
        j=bisect_left(stack,number)
        stack[j]=number
        index[i]=j+1

ans=[]
target=len(stack)
for k in range(N-1,-1,-1):
    if index[k]==target:
        ans.append(numbers[k])
        target-=1
        if target==0:
            break

print(len(stack))
print(*ans[::-1])
from bisect import bisect_left

N=int(input())
numbers=list(map(int,input().split()))

stack=[numbers[0]]

for number in numbers:
    if stack[-1]<number:
        stack.append(number)
    else:
        stack[bisect_left(stack,number)]=number

print(len(stack))
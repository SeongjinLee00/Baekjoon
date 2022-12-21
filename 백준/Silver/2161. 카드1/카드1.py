from collections import deque

numbers=deque([(i+1) for i in range(int(input()))])

ans=[]

while len(numbers)>=2:
    ans.append(str(numbers.popleft()))
    numbers.append(str(numbers.popleft()))

if ans: print(" ".join(ans),end=' ')
print(numbers[0])
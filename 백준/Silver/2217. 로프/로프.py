numbers=[]
N=int(input())

import sys
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
C=len(numbers)

ans=0

for number in numbers:
    if ans<C*number:
        ans=C*number

    C-=1

print(ans)
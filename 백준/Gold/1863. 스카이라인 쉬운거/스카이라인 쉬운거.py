import sys

input = sys.stdin.readline

N=int(input())

stack=[]
cnt=0
for _ in range(N):
    a,b=map(int,input().split())
    if not stack:
        stack.append(b)
        continue
    if b==stack[-1]:
        continue
    elif b>stack[-1]:
        stack.append(b)
    elif b<stack[-1]:
        while stack and b<stack[-1]:
            stack.pop()
            cnt+=1
        if not stack or (stack and not b==stack[-1]): stack.append(b)

while stack and 0<stack[-1]:
    stack.pop()
    cnt+=1
print(cnt)
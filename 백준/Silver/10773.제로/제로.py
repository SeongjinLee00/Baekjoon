import sys

N=int(input())

stack=[]

for _ in range(N):
    d=int(sys.stdin.readline())
    if d!=0:
        stack.append(d)
    elif d==0:
        stack.pop()

print(sum(stack))
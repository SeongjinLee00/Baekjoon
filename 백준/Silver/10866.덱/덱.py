from collections import deque

import sys
stack=deque([])

N=int(sys.stdin.readline())

for _ in range(N):
    s=sys.stdin.readline().split()
    if s[0]=='push_front':
        stack.appendleft(s[1])
    if s[0]=='push_back':
        stack.append(s[1])
    if s[0]=='pop_front':
        try:
            print(stack.popleft())
        except:
            print(-1)
    if s[0]=='pop_back':
        try:
            print(stack.pop())
        except:
            print(-1)
    if s[0]=='size':
        print(len(stack))
    if s[0]=='empty':
        try:
            stack[0] # 맨앞 원소를 호출해서 인덱스에러나면 1출력, 안나면 0출력
            print(0)
        except:
            print(1)
    if s[0]=='front':
        try:
            print(stack[0])
        except:
            print(-1)
    if s[0]=='back':
        try:
            print(stack[-1])
        except:
            print(-1)
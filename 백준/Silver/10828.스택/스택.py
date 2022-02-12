import sys
stack=[]

N=int(sys.stdin.readline())

for _ in range(N):
    s=sys.stdin.readline().split()
    if s[0]=='push':
        stack.append(s[1])
    if s[0]=='pop':
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
    if s[0]=='top':
        try:
            print(stack[-1])
        except:
            print(-1)
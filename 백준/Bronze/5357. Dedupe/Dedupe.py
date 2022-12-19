T=int(input())

for _ in range(T):
    s=input()
    stack=[]
    
    for c in s:
        if not stack or stack[-1]!=c:
            stack.append(c)
    
    print("".join(stack))
s=input()

ans=0

stack=[]

for c in s:
    if c=='(':
        stack.append(c)
    elif c=='H':
        stack.append(1)
    elif c=='C':
        stack.append(12)
    elif c=='O':
        stack.append(16)
    elif c==')':
        tmp=0
        while stack[-1]!='(':
            tmp+=stack.pop()
        stack.pop()
        stack.append(tmp)
    elif c.isnumeric():
        stack[-1]*=int(c)

print(sum(stack))
ss=input()
formula=''
stack=[]
for s in ss:
    if s=='(':
        stack.append(s)
    elif s==')':
        while stack[-1]!='(':
            formula+=stack.pop()
        stack.pop()
    elif s=='*' or s=='/':
        try:
            while stack[-1]=='*' or stack[-1]=='/':
                formula+=stack.pop()
            stack.append(s)
        except:
            stack.append(s)
    elif s=='+' or s=='-':
        try:
            while stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+' or stack[-1]=='-':
                formula+=stack.pop()
            stack.append(s)
        except:
            stack.append(s)
    else:
        formula+=s
while len(stack)!=0:
    formula+=stack.pop()

print(formula)
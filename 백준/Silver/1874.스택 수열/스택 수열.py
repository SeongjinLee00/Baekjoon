N=int(input())

stack=[0]
d=int(input())
i=1
cnt=0
incnt=1
ans=[]
while cnt<=N:
    if i>100002:
        print('NO')
        exit(0)
    if stack[-1]!=d:
        stack.append(i)
        ans.append('+')
        i+=1
    elif stack[-1]==d:
        stack.pop()
        ans.append('-')
        cnt+=1
        if cnt==N:
            break
        d=int(input())
        incnt+=1
if i<=100001:
    for a in ans:
        print(a)
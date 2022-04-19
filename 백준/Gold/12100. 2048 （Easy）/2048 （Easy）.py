from itertools import product

def move(case):
    if case==2:
        for i in range(N):
            stack=[]
            new_stack=[]
            for j in range(N):
                if board[i][j]!=0:
                    stack.append(board[i][j])
                    board[i][j]=0
            c=0
            l=len(stack)
            while True:
                if l==0:
                    break
                if l==1:
                    new_stack.append(stack[c])
                    break
                if stack[c]==stack[c+1]:
                    new_stack.append(2*stack[c])
                    c+=2
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
                    elif c==l:
                        break
                else:
                    new_stack.append(stack[c])
                    c+=1
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
            k=0
            while new_stack:
                board[i][k]=new_stack.pop(0)
                k+=1
    elif case==3:
        for i in range(N):
            stack=[]
            new_stack=[]
            for j in range(N-1,-1,-1):
                if board[i][j]!=0:
                    stack.append(board[i][j])
                    board[i][j]=0
            c=0
            l=len(stack)
            while True:
                if l==0:
                    break
                if l==1:
                    new_stack.append(stack[c])
                    break
                if stack[c]==stack[c+1]:
                    new_stack.append(2*stack[c])
                    c+=2
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
                    elif c==l:
                        break
                else:
                    new_stack.append(stack[c])
                    c+=1
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
            k=N-1
            while new_stack:
                board[i][k]=new_stack.pop(0)
                k-=1
    elif case==0:
        for i in range(N):
            stack=[]
            new_stack=[]
            for j in range(N):
                if board[j][i]!=0:
                    stack.append(board[j][i])
                    board[j][i]=0
            c=0
            l=len(stack)
            while True:
                if l==0:
                    break
                if l==1:
                    new_stack.append(stack[c])
                    break
                if stack[c]==stack[c+1]:
                    new_stack.append(2*stack[c])
                    c+=2
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
                    elif c==l:
                        break
                else:
                    new_stack.append(stack[c])
                    c+=1
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
            k=0
            while new_stack:
                board[k][i]=new_stack.pop(0)
                k+=1
    elif case==1:
        for i in range(N):
            stack=[]
            new_stack=[]
            for j in range(N-1,-1,-1):
                if board[j][i]!=0:
                    stack.append(board[j][i])
                    board[j][i]=0
            c=0
            l=len(stack)
            while True:
                if l==0:
                    break
                if l==1:
                    new_stack.append(stack[c])
                    break
                if stack[c]==stack[c+1]:
                    new_stack.append(2*stack[c])
                    c+=2
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
                    elif c==l:
                        break
                else:
                    new_stack.append(stack[c])
                    c+=1
                    if c==l-1:
                        new_stack.append(stack[c])
                        break
            k=N-1
            while new_stack:
                board[k][i]=new_stack.pop(0)
                k-=1

N=int(input())

board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

memory=[row[:] for row in board]

case=[0,1,2,3] # 상하좌우

order=product(case,case,case,case,case)

ans=0

for o in order:
    board=[row[:] for row in memory]
    for c in o:
        move(c)
    for i in range(N):
        for j in range(N):
            if board[i][j]>ans:
                ans=board[i][j]

print(ans)
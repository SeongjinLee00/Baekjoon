T=int(input())

for _ in range(T):
    s=list(input())

    left=0
    right=0
    while(len(s)!=0):
        if(s.pop())=='(':
            left+=1
        else:
            right+=1
        
        if left>right:
            print('NO')
            break
    if left==right:
        print('YES')
    elif left<right:
        print('NO')
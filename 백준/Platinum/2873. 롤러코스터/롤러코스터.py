R,C=map(int,input().split())

numbers=[]
for _ in range(R):
    numbers.append(list(map(int,input().split())))

if R%2:
    cnt=0
    ans=''

    for _ in range(R-1):
        if cnt%2:
            ans+='L'*(C-1)
            ans+='D'
            cnt+=1
        else:
            ans+='R'*(C-1)
            ans+='D'
            cnt+=1
    
    ans+='R'*(C-1)
    print(ans)

elif C%2:
    cnt=0
    ans=''

    for _ in range(C-1):
        if cnt%2:
            ans+='U'*(R-1)
            ans+='R'
            cnt+=1
        else:
            ans+='D'*(R-1)
            ans+='R'
            cnt+=1
    
    ans+='D'*(R-1)
    print(ans)

else:
    tmp=9999999
    target_r=0
    target_c=0
    for i in range(R):
        for j in range(C):
            if (i+j)%2:
                if numbers[i][j]<tmp:
                    tmp=numbers[i][j]
                    target_r=i
                    target_c=j

    ans=''
    my_r=0
    my_c=0
    flag=0

    while True:
        if my_r>=target_r+2:
            flag=1
        if (target_r%2==0 and my_r!=target_r) and (target_r%2==0 and my_r!=target_r+1) or (target_r%2==1 and my_r!=target_r-1) and (target_r%2==1 and my_r!=target_r):
            if not flag:
                ans+='R'*(C-1)
                ans+='D'
            else:
                ans+='D'
                ans+='R'*(C-1)
            my_c+=(C-1)
            my_r+=1
            if my_r==R-1 and my_c==C-1:
                print(ans)
                exit(0)
            if not flag:
                ans+='L'*(C-1)
                ans+='D'
            else:
                ans+='D'
                ans+='L'*(C-1)
            my_c-=(C-1)
            my_r+=1
        else:
            if my_r%2==0 and my_c%2==0:
                if my_r+1==target_r and my_c==target_c:
                    ans+='R'
                    my_c+=1
                    flag=1
                else:
                    if not flag:
                        ans+='D'
                        my_r+=1
                    else:
                        ans+='R'
                        my_c+=1
            elif my_r%2==0 and my_c%2==1:
                if not flag:
                    ans+='R'
                    my_c+=1
                else:
                    ans+='D'
                    my_r+=1
            elif my_r%2==1 and my_c%2==0:
                if not flag:
                    ans+='R'
                    my_c+=1
                else:
                    ans+='U'
                    my_r-=1
            else:
                if my_r-1==target_r and my_c==target_c:
                    ans+='R'
                    my_c+=1
                    flag=1
                else:
                    if not flag:
                        ans+='U'
                        my_r-=1
                    else:
                        ans+='R'
                        my_c+=1
        
            if my_c==C-1 and my_r%2==1:
                if my_r==R-1:
                    print(ans)
                    exit(0)
                else:
                    ans+='D'
                    ans+='L'*(C-1)
                    my_r+=1
                    my_c-=(C-1)
        
        if my_r==R-1 and my_c==C-1:
            print(ans)
            exit(0)
from collections import deque

T=int(input())

for _ in range(T):
    p=list(input())
    n=int(input())
    numbers=input()
    numbers2=numbers
    case=0
    ans=0
    d=0
    r=0


    if numbers=='[]': # 경우 1
        case=1
    elif ',' not in numbers: # 경우 2
        case=2
    else:
        numbers=numbers.split(',')
        numbers[0]=numbers[0][1:]
        numbers[-1]=numbers[-1][:-1]
    
    numbers=deque(numbers)


    for s in p:
        if case==1:
            if s=='R':
                pass
            elif s=='D':
                ans='error'
                break
        
        elif case==2:
            if s=='R':
                pass
            elif s=='D':
                if d==0:
                    ans='[]'
                    d+=1
                elif d==1:
                    ans='error'
                    break
        
        else:
            if s=='R':
                r+=1
            elif s=='D':
                try:
                    if r%2:
                        numbers.pop()
                    else:
                        numbers.popleft()
                except:
                    ans='error'
                    break

    if case==0 and r%2==1:
        numbers.reverse()

    if case==1:
        if ans=='error':
            print(ans)
        else:
            print('[]')
    elif case==2:
        if ans=='error':
            print(ans)
        elif ans=='[]':
            print(ans)
        else:
            print(numbers2)
    else:
        if ans=='error':
            print(ans)
        elif numbers==deque([]):
            print('[]')
        else:
            print('[',end='')
            for i in range(len(numbers)-1):
                print(numbers[i],end=',')
            print(numbers[-1],end=']')
            print()

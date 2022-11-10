from collections import deque

primes=[False,False]+[True]*9998

for i in range(2,101):
    if primes[i]:
        for j in range(2*i,10000,i):
            primes[j]=False

T=int(input())

for _ in range(T):
    now,target=map(int,input().split())

    q=deque([[now,0]])

    visited=[0]*10000

    visited[now]=1

    flag=False

    while q:
        now,d=q.popleft()
        if now==target:
            print(d)
            flag=True
            break
        memory=now
        for i in range(10):
            now-=int(str(now)[0])*1000
            test1=now+1000*i
            now=memory

            now-=int(str(now)[1])*100
            test3=now+100*i
            now=memory

            now-=int(str(now)[2])*10
            test5=now+10*i
            now=memory

            now-=int(str(now)[3])
            test7=now+i
            now=memory

            if 1000<=test1<=9999 and primes[test1] and not visited[test1]:
                q.append([test1,d+1])
                visited[test1]=1

            if 1000<=test3<=9999 and primes[test3] and not visited[test3]:
                q.append([test3,d+1])
                visited[test3]=1

            if 1000<=test5<=9999 and primes[test5] and not visited[test5]:
                q.append([test5,d+1])
                visited[test5]=1

            if 1000<=test7<=9999 and primes[test7] and not visited[test7]:
                q.append([test7,d+1])
                visited[test7]=1

    if not flag:
        print('Impossible')
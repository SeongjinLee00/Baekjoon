S=int(input())
switches=['switch']
temp=map(int,input().split())
switches=switches+list(temp)

def operate(num):
    # global switches
    if switches[num]==0:
        switches[num]=1
    elif switches[num]==1:
        switches[num]=0

N=int(input())

for _ in range(N):
    a,b = map(int,input().split())
    if a==1:
        for i in range(1,S+1):
            if i%b==0:
                operate(i)

    if a==2:
        operate(b)
        for k in range(1, min(b,S-b+1)):
            if switches[b-k]==switches[b+k]:
                operate(b-k)
                operate(b+k)
            else:
                break

switches.remove('switch')

try:
    for i in range(20):
        print(switches[i],end=' ')
    print('')
    for j in range(20,40):
        print(switches[j],end=' ')
    print('')
    for k in range(40,60):
        print(switches[k],end=' ')
    print('')
    for l in range(60,80):
        print(switches[l],end=' ')
    print('')
    for m in range(80,100):
        print(switches[m],end=' ')
except:
    pass
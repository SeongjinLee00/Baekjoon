import sys
input=sys.stdin.readline

N=int(input())
tmp=[]

res=0
maxres=0

def gcd(num1,num2): # Euclidian 
    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    r=a%b
    if a%b==0:
        return b
    else:
        return gcd(b,r)

for _ in range(N):
    a,b=map(int,input().split())
    if a>0:
        if a+res!=b:
            print(-1)
            exit(0)
        res=b
    else:
        if -a>res:
            tmp.append(b-a-res)
            res=b
            if res>maxres:
                maxres=res
        else:
            if a+res!=b:
                print(-1)
                exit(0)
        res=b

if len(tmp)==0:
    print(1)
elif len(tmp)==1:
    if tmp[0]>9*(10**18):
        raise EOFError
    if tmp[0]<=maxres:
        print(-1)
        exit(0)
    print(tmp[0])
else:
    G=gcd(tmp[0],tmp[1])
    for i in range(len(tmp)-1):
        if gcd(tmp[i],tmp[i+1])<G:
            G=gcd(tmp[i],tmp[i+1])
    
    if G>maxres:
        print(G)
    else:
        print(-1)
N,M=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
result=[]
for a in A:
    if a in B:
        if a not in result:
            print(a)
            result.append(a)
N=int(input())

A=list(map(int,input().split()))
A.sort()

ans=0
B=A[::]
for i in range(N):
    left=0
    right=N-2
    d=A[i]
    B=A[::]
    B.remove(d)
    while left<right:
        add=B[left]+B[right]
        if add==d:
            ans+=1
            break
        elif add>d:
            right-=1
        else:
            left+=1

print(ans)
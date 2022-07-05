import sys

input=sys.stdin.readline

N=int(input())

m,n=map(int,input().split())

A=[]
B=[]

for _ in range(m):
    A.append(int(input()))

for _ in range(n):
    B.append(int(input()))

A+=A
B+=B

left=[]
right=[]

# print(A)
# print(B)

for i in range(len(A)//2):
    tmp=0
    for j in range(i,len(A)//2+i-1):
        tmp+=A[j]
        left.append(tmp)

for i in range(len(B)//2):
    tmp=0
    for j in range(i,len(B)//2+i-1):
        tmp+=B[j]
        right.append(tmp)

left.append(sum(A)//2)
right.append(sum(B)//2)
# print(left)
# print(right)
left.sort()
right.sort()

left=[0]+left
right=[0]+right
i=0
j=len(right)-1

ans=0

# print(left)
# print(right)
while True:
    tmp=left[i]+right[j]
    # print(left[i],right[j],tmp)
    if tmp>N:
        j-=1
    elif tmp<N:
        i+=1
    else:
        ans+=1
        if i<=len(left)-2 and left[i]==left[i+1] and right[j]==right[j-1]:
            tmp1=left[i]
            cnt1=0
            while left[i]==tmp1:
                i+=1
                cnt1+=1
            tmp2=right[j]
            cnt2=0
            while right[j]==tmp2:
                j-=1
                cnt2+=1
            ans+=(cnt1*cnt2-1)
        elif right[j]==right[j-1]:
            j-=1
        else:
            i+=1

    if i==len(left) or j==-1:
        break

print(ans)
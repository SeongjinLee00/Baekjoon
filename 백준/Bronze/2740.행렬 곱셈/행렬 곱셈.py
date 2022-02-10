def innerproduct(list1,list2):
    sum=0
    for i in range(len(list1)):
        sum+=list1[i]*list2[i]

    return sum

N, M=map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int,input().split())))

B=[]
M, K=map(int,input().split())
for _ in range(M):
    B.append(list(map(int,input().split())))

B=list(zip(*B))

for i in range(N):
    for j in range(K):
        print(innerproduct(A[i],B[j]),end=' ')
    print('')
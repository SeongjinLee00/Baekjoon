from itertools import permutations

N,M,K=map(int,input().split())

numbers=[]
for _ in range(N):
    numbers.append(list(map(int,input().split())))

numbers_original=[row[:] for row in numbers]

rotations=[]
for _ in range(K):
    rotations.append(list(map(int,input().split())))

def rotate(arr):
    K=len(arr[0])
    original=[row[:] for row in arr]
    new=[[0]*K for _ in range(K)]
    
    for k in range(K//2):
        for j in range(1+k,K-k):
            new[0+k][j]=original[0+k][j-1]
        for i in range(1+k,K-k):
            new[i][K-1-k]=original[i-1][K-1-k]
        for j in range(K-2-k,-1+k,-1):
            new[K-1-k][j]=original[K-1-k][j+1]
        for i in range(K-2-k,-1+k,-1):
            new[i][0+k]=original[i+1][0+k]
    new[K//2][K//2]=original[K//2][K//2]
    return new
ans=99999999999999999
for item in permutations(rotations,K):
    numbers=[row[:] for row in numbers_original]
    for rotation in item:
        r,c,s=rotation
        r-=1
        c-=1
        target=[row[c-s:c+s+1] for row in numbers[r-s:r+s+1]]
        rotation_target=rotate(target)
        for i in range(r-s,r+s+1):
            for j in range(c-s,c+s+1):
                numbers[i][j]=rotation_target[i-(r-s)][j-(c-s)]
    
    for row in numbers:
        temp=sum(row)
        if temp<ans:
            ans=temp

print(ans)
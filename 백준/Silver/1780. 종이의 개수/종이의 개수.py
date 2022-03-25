K=int(input())

paper=[]

for _ in range(K):
    paper.append(list(map(int,input().split())))

minus=0
zero=0
plus=0

def divide(arr,N):
    
    global minus
    global zero
    global plus

    number=arr[0][0]
    flag=0
    for i in range(N):
        for j in range(N):
            if arr[i][j]!=number:
                flag=1
                break
        if flag:
            break

    if not flag:
        if number==1:
            plus+=1
        elif number==0:
            zero+=1
        elif number==-1:
            minus+=1

    else:
        arr1=[row[0:N//3] for row in arr[0:N//3]]
        divide(arr1,N//3)
        arr2=[row[0:N//3] for row in arr[N//3:2*N//3]]
        divide(arr2,N//3)
        arr3=[row[0:N//3] for row in arr[2*N//3:N]]
        divide(arr3,N//3)
        arr4=[row[N//3:2*N//3] for row in arr[0:N//3]]
        divide(arr4,N//3)
        arr5=[row[N//3:2*N//3] for row in arr[N//3:2*N//3]]
        divide(arr5,N//3)
        arr6=[row[N//3:2*N//3] for row in arr[2*N//3:N]]
        divide(arr6,N//3)
        arr7=[row[2*N//3:N] for row in arr[0:N//3]]
        divide(arr7,N//3)
        arr8=[row[2*N//3:N] for row in arr[N//3:2*N//3]]
        divide(arr8,N//3)
        arr9=[row[2*N//3:N] for row in arr[2*N//3:N]]
        divide(arr9,N//3)

divide(paper,K)

print(minus)
print(zero)
print(plus)
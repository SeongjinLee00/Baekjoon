N=int(input())

data=[]

for _ in range(N):
    data.append(list(map(int,list(input()))))

ans=''
def divide(arr,N):

    global ans

    if sum(sum(arr,[]))==N*N:
        ans+='1'
        return

    elif sum(sum(arr,[]))==0:
        ans+='0'
        return

    else:
        ans+='('
        arr1=[row[0:N//2] for row in arr[0:N//2]]
        divide(arr1,N//2)
        arr2=[row[N//2:N] for row in arr[0:N//2]]
        divide(arr2,N//2)
        arr3=[row[0:N//2] for row in arr[N//2:N]]
        divide(arr3,N//2)
        arr4=[row[N//2:N] for row in arr[N//2:N]]
        divide(arr4,N//2)
        ans+=')'

divide(data,N)
print(ans)
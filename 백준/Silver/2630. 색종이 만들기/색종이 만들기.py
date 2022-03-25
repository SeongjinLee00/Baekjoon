N=int(input())

paper=[]

for _ in range(N):
    paper.append(list(map(int,input().split())))

white=0
blue=0

def divide(arr,N):
    
    global white
    global blue

    l=len(arr[0])
    
    if sum(sum(arr,[]))==l*l:
        blue+=1
        return
    
    elif sum(sum(arr,[]))==0:
        white+=1
        return
    
    else:
        arr1=[row[0:N//2] for row in arr[0:N//2]]
        divide(arr1,N//2)
        arr2=[row[0:N//2] for row in arr[N//2:N]]
        divide(arr2,N//2)
        arr3=[row[N//2:N] for row in arr[0:N//2]]
        divide(arr3,N//2)
        arr4=[row[N//2:N] for row in arr[N//2:N]]
        divide(arr4,N//2)

divide(paper,N)
print(white)
print(blue)
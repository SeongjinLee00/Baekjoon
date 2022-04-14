from bisect import bisect_left

N=int(input())

numbers=list(map(int,input().split()))

numbers.sort()

ans=0
for k in range(N-2):
    i=k+1
    j=N-1
    
    while i<j:
        partialsum=numbers[k]+numbers[i]+numbers[j]
        if partialsum==0:
            if numbers[i]==numbers[j]:
                ans+=(j-i+1)*(j-i)//2
                break
            else:
                idx=bisect_left(numbers, numbers[j])
                ans+=j-idx+1
                i+=1
        elif partialsum<0:
            i+=1
        elif partialsum>0:
            j-=1

print(ans)
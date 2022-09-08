N=int(input())
numbers=list(map(int,input().split()))

numbers.sort()

if N%2:
    ans=numbers[-1]
    numbers.pop()
    N-=1
else:
    ans=-1
    
for k in range(N//2):
    if numbers[k]+numbers[N-k-1]>ans:
        ans=numbers[k]+numbers[N-k-1]
print(ans)
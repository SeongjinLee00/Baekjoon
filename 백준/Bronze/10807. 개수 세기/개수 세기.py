N=int(input())
numbers=list(map(int,input().split()))
o=int(input())
ans=0
for number in numbers:
    if number==o:
        ans+=1
print(ans)
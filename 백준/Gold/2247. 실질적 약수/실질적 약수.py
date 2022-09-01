ans=0
n=int(input())
for i in range(2,int(n**0.5)+1):
    j=n//i
    ans+=(i+j)*(j-i+1)//2
    ans+=i*(j-i)

print(ans%1000000)
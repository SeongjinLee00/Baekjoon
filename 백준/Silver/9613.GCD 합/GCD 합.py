def gcd(num1,num2): # Euclidian 

    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1

    r=a%b

    if a%b==0:
        return b
    else:
        return gcd(b,r)
T=int(input())
for _ in range(T):
    sum=0
    N, *numbers=list(map(int,input().split()))

    for i in range(N):
        for j in range(i+1,N):
            sum+=gcd(numbers[i],numbers[j])
    
    print(sum)
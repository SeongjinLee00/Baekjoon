def solution(n):
    fibo=[0]*100001
    fibo[1]=1
    fibo[2]=1
    
    for k in range(3,100001):
        fibo[k]=(fibo[k-1]+fibo[k-2])%1234567
    
    return fibo[n]
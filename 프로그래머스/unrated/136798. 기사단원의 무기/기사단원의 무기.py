def divisors(n):
    ret=0
    num=0
    for num in range(1,int(n**0.5)+1):
        if n%num==0:
            ret+=2
    if (num)*(num)==n:
        ret-=1
    
    return ret

def solution(number, limit, power):
    ds=[0]*number
    
    for num in range(1,number+1):
        ds[num-1]=divisors(num)
        
    ans=0
    for num in ds:
        if num>limit:
            ans+=power
        else:
            ans+=num
    
    return ans
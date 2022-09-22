# primes=[1]*1000001
# primes[0]=0
# primes[1]=0

# for k in range(2,1002):
#     if not primes[k]:
#         continue
#     for l in range(2*k,1000001,k):
#         primes[l]=0

def is_prime(n):
    if n==1:
        return False
    for num in range(2,int(n**0.5)+1):
        if not n%num and not n==num:
            return False
    return True

def convert(n,k):
    ret=''
    
    while True:
        ret+=str(n%k)
        n//=k
        if n==0:
            return ret[::-1]

def solution(n, k):
    ans=0
    tmp=convert(n,k).split('0')
    for item in tmp:
        if not item:
            continue
        if is_prime(int(item)):
            ans+=1
    return ans
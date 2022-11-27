def solution(n):
    ans=''
    while True:
        n-=1
        ans+='124'[n%3]
        n//=3
        
        if n<=0:
            break
    
    return ans[::-1]
def solution(n):
    cnt=0
    
    for k in range(1,n+1):
        tmp=0
        while True:
            tmp+=k
            k+=1
            if tmp==n:
                cnt+=1
                break
            if tmp>n:
                break
    return cnt
def check(min):
    tmp=0
    for time in times:
        tmp+=(min//time)
        if tmp>=n:
            return True
    
    return False
        
def solution(n, times):
    lo=-1
    hi=10**20+1
    
    def check(min):
        tmp=0
        for time in times:
            tmp+=(min//time)
            if tmp>=n:
                return True

        return False
    
    while True:
        mid=(lo+hi)//2
        if check(mid):
            hi=mid
        else:
            lo=mid
            
        if lo+1==hi:
            return hi
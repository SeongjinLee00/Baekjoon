def solution(n, m, section):
    now=section[-1]
    
    ans=0
    
    while True:
        ans+=1
        while section and section[-1]>(now-m):
            section.pop()
            
        if not section:
            return ans
        
        now=section[-1]
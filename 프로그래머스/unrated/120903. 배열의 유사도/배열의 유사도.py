def solution(s1, s2):
    ans=0
    
    for item in s2:
        if item in s1:
            ans+=1
            
    return ans
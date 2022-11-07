from itertools import combinations

def solution(number):
    ans=0
    
    for item in combinations(number,3):
        if sum(item)==0:
            ans+=1
    
    return ans
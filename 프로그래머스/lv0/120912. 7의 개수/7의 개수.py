def solution(array):
    ans=0
    
    for num in array:
        ans+=str(num).count('7')
    
    return ans
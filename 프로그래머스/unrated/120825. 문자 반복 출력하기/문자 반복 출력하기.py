def solution(my_string, n):
    ans = ''
    for c in my_string:
        ans+=c*n
    
    return ans
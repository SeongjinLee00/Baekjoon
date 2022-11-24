def solution(n):
    ans=[i+1 for i in range(200)]
    for num in range(1,201):
        if num%3==0 or ('3' in str(num)):
            ans.remove(num)
    
    return ans[n-1]
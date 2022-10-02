def solution(array):
    ans=[-1,-1]
    for i in range(len(array)):
        if array[i]>ans[0]:
            ans=[array[i],i]
            
    return ans
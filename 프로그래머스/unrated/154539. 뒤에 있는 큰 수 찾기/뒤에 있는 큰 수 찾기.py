def solution(numbers):
    stack=[]
    
    ans=[0]*len(numbers)
    
    for idx, num in enumerate(numbers):
        if not stack or stack[-1][1]>=num:
            stack.append([idx,num])
        else:
            while stack and stack[-1][1]<num:
                ans[stack[-1][0]]=num
                stack.pop()
            stack.append([idx,num])
    
    for i in range(len(ans)):
        if ans[i]==0: ans[i]=-1
    
    return ans
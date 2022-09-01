def solution(target):
    cnt=0
    ans=''
    def dfs(word):
        nonlocal cnt
        nonlocal ans
        
        if word==target:
            ans=cnt
        if len(word)==5:
            return
        
        cnt+=1
        dfs(word+'A')
        cnt+=1
        dfs(word+'E')
        cnt+=1
        dfs(word+'I')
        cnt+=1
        dfs(word+'O')
        cnt+=1
        dfs(word+'U')
    
    dfs('')
    
    return ans
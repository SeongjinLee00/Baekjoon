def solution(cards):
    lens=[]
    
    def dfs(path):
        nonlocal lens
        next=cards[path[-1]]
        
        if path[0]==next-1:
            lens.append(len(path))
            return
        if not visited[next-1]:
            visited[next-1]=1
            path.append(next-1)
            dfs(path)
    
    visited=[0]*len(cards)
    
    for i in range(len(cards)):
        if not visited[i]:
            visited[i]=1
            dfs([i])
    if len(lens)==1:
        return 0
    lens.sort()
    return lens[-1]*lens[-2]
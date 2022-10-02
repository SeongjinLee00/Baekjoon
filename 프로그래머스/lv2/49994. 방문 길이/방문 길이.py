def solution(dirs):
    visited=set()
    
    r=0
    c=0
    for s in dirs:
        if s=='D':
            if r==5:
                continue
            visited.add(((r,c),(r+1,c)))
            visited.add(((r+1,c),(r,c)))
            r+=1
        elif s=='U':
            if r==-5:
                continue
            visited.add(((r,c),(r-1,c)))
            visited.add(((r-1,c),(r,c)))
            r-=1
        elif s=='R':
            if c==5:
                continue
            visited.add(((r,c),(r,c+1)))
            visited.add(((r,c+1),(r,c)))
            c+=1
        elif s=='L':
            if c==-5:
                continue
            visited.add(((r,c),(r,c-1)))
            visited.add(((r,c-1),(r,c)))
            c-=1
    
    return len(visited)//2
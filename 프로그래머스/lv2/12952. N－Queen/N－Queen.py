def solution(n):
    answer = 0
    
    def backtrack(rows,cols,queens):
        nonlocal answer

        if len(queens)==n:
            answer+=1
            return
        
        for next in range(len(queens)*n,len(queens)*n+n):
            r=next//n
            c=next%n
            
            if not rows[r] and not cols[c]:
                for k in range(-r,0):
                    if 0<=r+k<n and 0<=c+k<n and (r+k,c+k) in queens:
                        break
                    if 0<=r+k<n and 0<=c-k<n and (r+k,c-k) in queens:
                        break
                else:
                    rows[r]=1
                    cols[c]=1
                    queens.add((r,c))
                    backtrack(rows,cols,queens)
                    rows[r]=0
                    cols[c]=0
                    queens.remove((r,c))
    
    backtrack([0]*n,[0]*n,set())
    return answer
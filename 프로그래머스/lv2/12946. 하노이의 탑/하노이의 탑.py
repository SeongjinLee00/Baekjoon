def solution(n):
    answer=[]
    def move(howmany, start, end, remainder):
        if howmany==1:
            answer.append([start,end])
            return
        else:
            move(howmany-1, start, remainder, end)
            move(1, start, end, remainder)
            move(howmany-1, remainder, end, start)
    
    move(n,1,3,2)
    
    return answer
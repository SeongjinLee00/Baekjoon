def solution(n):
    answer = [[0]*(_+1) for _ in range(n)]
    M=n*(n+1)//2
    num=0
    row=-1
    col=0
    len=n
    
    while True:
        for _ in range(len):
            row+=1
            num+=1
            answer[row][col]=num
        len-=1
        if len==0:
            break
        for _ in range(len):
            num+=1
            col+=1
            answer[row][col]=num
        len-=1
        if len==0:
            break
        for _ in range(len):
            num+=1
            row-=1
            col-=1
            answer[row][col]=num
        len-=1
        if len==0:
            break
    
    ret=[]
    
    for item in answer:
        ret.extend(item)

    return ret
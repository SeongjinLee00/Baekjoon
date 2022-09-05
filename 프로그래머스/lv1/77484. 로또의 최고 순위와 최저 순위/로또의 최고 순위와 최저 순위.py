def solution(lottos, win_nums):
    match=0
    
    for num in lottos:
        if num in win_nums:
            match+=1
    
    d={6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    
    return [d[match+lottos.count(0)], d[match]]
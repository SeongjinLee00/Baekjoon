def solution(names, yearning, photo):
    answer = []
    
    for item in photo:
        num=0
        for name in item:
            if name not in names:continue
            num+=yearning[names.index(name)]
        
        answer.append(num)
    
    return answer
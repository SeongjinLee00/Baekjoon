from bisect import bisect_left
from collections import defaultdict

def solution(info, query):
    d=defaultdict(list)
    
    for item in info:
        language,position,career,food,score=item.split()
        
        d[language[0]+position[0]+career[0]+food[0]].append(int(score))
    
    for key in d.keys():
        d[key].sort()
    
    ret=[]
    for item in query:
        language, and1, position, and2, career, and3, food, score = item.split()
        
        result=0
        
        for lan in ['c','j','p']:
            if language!='-' and language[0]!=lan:
                continue
            for pos in ['b','f']:
                if position!='-' and position[0]!=pos:
                    continue
                for car in ['j','s']:
                    if career!='-' and career[0]!=car:
                        continue
                    for foo in ['c','p']:
                        if food!='-' and food[0]!=foo:
                            continue
                        result+=len(d[lan+pos+car+foo])-bisect_left(d[lan+pos+car+foo],int(score))
        ret.append(result)
    
    return ret
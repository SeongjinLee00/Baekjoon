def solution(record):
    d=dict()
    for item in record:
        item2=item.split()
        
        if item2[0]=='Enter' or item2[0]=='Change':
            uid, nickname = item2[1],item2[2]
            d[uid]=nickname
    
    ret=[]
    
    for item in record:
        item2=item.split()
        
        if item2[0]=='Enter':
            uid=item2[1]
            ret.append(d[uid]+'님이 들어왔습니다.')
        elif item2[0]=='Leave':
            uid=item2[1]
            ret.append(d[uid]+'님이 나갔습니다.')
            
    return ret
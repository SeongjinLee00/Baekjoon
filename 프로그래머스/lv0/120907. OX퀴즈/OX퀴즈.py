def solution(quiz):
    result=[]
    for item in quiz:
        item=item.split()
        if item[1]=='-':
            if int(item[0])-int(item[2])==int(item[4]):
                result.append('O')
            else:
                result.append('X')
        else:
            if int(item[0])+int(item[2])==int(item[4]):
                result.append('O')
            else:
                result.append('X')
    
    return result
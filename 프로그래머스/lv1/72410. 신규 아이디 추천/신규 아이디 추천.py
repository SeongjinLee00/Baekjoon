def solution(new_id):
    new_id = new_id.lower()
    
    tmp2=''
    p={'-', '_', '.'}
    for c in new_id:
        if c in p or c.isnumeric() or c.isalpha():
            tmp2+=c
    
    tmp3=''
    i=0
    while i<len(tmp2):
        if tmp2[i]=='.':
            tmp3+='.'
            while True:
                i+=1
                if i>=len(tmp2) or tmp2[i]!='.':
                    break
        else:
            tmp3+=tmp2[i]
            i+=1
    
    if tmp3[0]=='.':
        tmp3=tmp3[1:]
    if tmp3 and tmp3[-1]=='.':
        tmp3=tmp3[:len(tmp3)-1]

    if not tmp3:
        tmp3='a'
    
    if len(tmp3)>=16:
        tmp3=tmp3[:15]
    
    if tmp3[-1]=='.':
        tmp3=tmp3[:len(tmp3)-1]
    
    if len(tmp3)<=2:
        tmp3+=tmp3[-1]*(3-len(tmp3))
    
    return tmp3
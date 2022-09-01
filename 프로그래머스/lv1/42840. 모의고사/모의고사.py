def solution(answers):
    one=[1,2,3,4,5]*2000
    two=[2,1,2,3,2,4,2,5]*1250
    three=[3,3,1,1,2,2,4,4,5,5]*1000
    
    a=0
    b=0
    c=0
    
    for i in range(len(answers)):
        if answers[i]==one[i]:
            a+=1
        if answers[i]==two[i]:
            b+=1
        if answers[i]==three[i]:
            c+=1
            
    ret=[]
    
    if max([a,b,c])==a:
        ret.append(1)
    if max([a,b,c])==b:
        ret.append(2)
    if max([a,b,c])==c:
        ret.append(3)
        
    return ret
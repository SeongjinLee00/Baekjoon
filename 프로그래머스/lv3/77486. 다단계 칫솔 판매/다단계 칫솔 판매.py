def solution(enroll, referral, seller, amount):
    d=dict() # name to index
    
    cnt=0
    for name in enroll:
        d[name]=cnt
        cnt+=1
    result=[0]*len(enroll)
    
    for i in range(len(seller)):
        name=seller[i]
        money=amount[i]*100
        
        while True:
            result[d[name]]+=(money-money//10)
            if referral[d[name]]=='-':
                break

            name=referral[d[name]]
            money//=10
            if money==0:
                break

    return result
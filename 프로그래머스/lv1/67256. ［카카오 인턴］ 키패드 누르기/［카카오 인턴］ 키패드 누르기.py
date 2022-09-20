def solution(numbers, hand):
    ans=''
    
    Lr=3
    Lc=0
    Rr=3
    Rc=2
    
    for number in numbers:
        if number in [1,4,7]:
            ans+='L'
            Lr=number//3
            Lc=0
        elif number in [3,6,9]:
            ans+='R'
            Rr=number//3-1
            Rc=2
        else:
            if number==2:
                Tr=0
                Tc=1
            elif number==5:
                Tr=1
                Tc=1
            elif number==8:
                Tr=2
                Tc=1
            elif number==0:
                Tr=3
                Tc=1
            LD=abs(Lr-Tr)+abs(Lc-Tc)
            RD=abs(Rr-Tr)+abs(Rc-Tc)
            
            if LD>RD:
                ans+='R'
                Rr=Tr
                Rc=Tc
            elif LD<RD:
                ans+='L'
                Lr=Tr
                Lc=Tc
            else:
                if hand=='right':
                    ans+='R'
                    Rr=Tr
                    Rc=Tc
                else:
                    ans+='L'
                    Lr=Tr
                    Lc=Tc

    return ans
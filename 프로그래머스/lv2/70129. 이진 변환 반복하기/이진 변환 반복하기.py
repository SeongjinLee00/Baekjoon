def solution(s):
    c1=0
    c2=0
    def remove_zero(s1):
        nonlocal c2
        cc=s1.count('0')
        c2+=cc
        return '1'*(len(s1)-cc)
    
    def bin_to_dec(s2):
        nonlocal c1
        c1+=1
        ret=''
        s2=len(s2)
        while True:
            ret+=str(s2%2)
            s2//=2
            if s2==0:
                return ret[::-1]
    
    while True:
        if s=='1':
            return [c1,c2]
        else:
            s=remove_zero(s)
            s=bin_to_dec(s)
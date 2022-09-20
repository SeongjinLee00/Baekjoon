def solution(n):
    a=''
    
    f=0
    for i in range(1000,-1,-1):
        if (3**i)<=n:
            f=1
        if f and (3**i)<=n:
            a+=str(n//(3**i))
            n-=(3**i)*int(a[-1])
        elif f and (3**i)>n:
            a+='0'
    a=a
    ret=0
    
    for i in range(len(a)):
        ret+=(3**i)*int(a[i])
    return ret
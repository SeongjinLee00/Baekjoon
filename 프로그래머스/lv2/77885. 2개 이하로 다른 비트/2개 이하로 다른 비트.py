def solution(numbers):
    result = []
    
    for num in numbers:
        now = '000'+bin(num)[2:]
        
        if now[-1]=='0':
            result.append(int(now[:-1]+'1',2))
        elif now[-2]=='0' and now[-1]=='0':
            result.append(int(now[:-2]+'11',2))
        else:
            idx=len(now)-1
            while now[idx]=='1':
                idx-=1
            result.append(int(now[:idx]+'10'+now[idx+2:],2))

    return result
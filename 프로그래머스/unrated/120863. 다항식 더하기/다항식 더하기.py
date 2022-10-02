def solution(polynomial):
    a=0
    b=0
    tmp=polynomial.split()
    
    for item in tmp:
        if item[-1]=='x':
            if len(item)==1:
                a+=1
            else:
                a+=int(item[:len(item)-1])
        elif item.isnumeric():
            b+=int(item)
    
    if a and b:
        if a==1:
            return f'x + {b}'
        return f'{a}x + {b}'
    elif a:
        if a==1:
            return 'x'
        return f'{a}x'
    elif b:
        return f'{b}'
    else:
        return '0'
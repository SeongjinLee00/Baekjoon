def solution(n, arr1, arr2):
    a1=['' for _ in range(n)]
    a2=['' for _ in range(n)]
    
    for i in range(n):
        num=int(arr1[i])
        for k in range(n-1,-1,-1):
            if num>=2**k:
                num-=2**k
                a1[i]+='#'
            else:
                a1[i]+=' '
    
    for i in range(n):
        num=int(arr2[i])
        for k in range(n-1,-1,-1):
            if num>=2**k:
                num-=2**k
                a2[i]+='#'
            else:
                a2[i]+=' '
            
    ret=['' for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if a1[i][j]=='#' or a2[i][j]=='#':
                ret[i]+=('#')
            else:
                ret[i]+=(' ')
                
    return ret
def solution(arr1, arr2):
    def innerproduct(vec1, vec2):
        ret=0
        for i in range(len(vec1)):
            ret+=vec1[i]*vec2[i]
        
        return ret
    
    r1=len(arr1)
    c1=len(arr1[0])
    
    r2=len(arr2)
    c2=len(arr2[0])
    
    ret=[[0]*c2 for _ in range(r1)]
    arr2=list(zip(*arr2))

    for i in range(r1):
        for j in range(c2):
            ret[i][j]=innerproduct(arr1[i],arr2[j])
            
    return ret
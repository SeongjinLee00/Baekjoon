def solution(arr):
    N=len(arr)
    ans=[0,0]
    
    def quad(r,c,i):
        tmp=0
        for x in range(r,r+i):
            for y in range(c,c+i):
                tmp+=arr[x][y]

        if tmp==i*i:
            ans[1]+=1
            return
        elif tmp==0:
            ans[0]+=1
            return
        quad(r,c,i//2)
        quad(r+i//2,c,i//2)
        quad(r,c+i//2,i//2)
        quad(r+i//2,c+i//2,i//2)
    
    quad(0,0,N)
    
    return ans
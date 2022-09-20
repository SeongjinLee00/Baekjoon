N=int(input())
K=int(input())

start=0
end=N*N+1

def smaller(M):
    ret=0
    for row in range(N,0,-1):
        ret+=min(N,M//row)

    return ret

while True:
    mid=(start+end)//2

    if smaller(mid)>=K:
        end=mid
    else:
        start=mid
    
    if start+1==end:
        print(end)
        exit(0)
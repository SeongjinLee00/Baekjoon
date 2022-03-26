N,r,c=map(int,input().split())

ans=0
def solve(r,c,N):
    
    global ans

    K=(2**N)

    if K==1:
        return
    
    if r<K//2 and c<K//2:
        solve(r,c,N-1)
    
    elif r<K//2 and c>=K//2:
        ans+=(4**(N-1))
        solve(r,c-K//2,N-1)

    elif r>=K//2 and c<K//2:
        ans+=2*(4**(N-1))
        solve(r-K//2,c,N-1)

    elif r>=K//2 and c>=K//2:
        ans+=3*(4**(N-1))
        solve(r-K//2,c-K//2,N-1)

solve(r,c,N)
print(ans)
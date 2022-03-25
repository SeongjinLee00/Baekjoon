K=int(input())

cnt=0
def solve(k):

    global cnt
    if k==1:
        if cnt%2==0:
            return 0
        else:
            return 1
    elif k==2:
        if cnt%2==0:
            return 1
        else:
            return 0
    else:
        for i in range(100):
            if k<=(2**i):
                break
        k-=(2**(i-1))
        cnt+=1
        return solve(k)

print(solve(K))
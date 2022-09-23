N,K=map(int,input().split())
cnt=0
def backtrack(s,arr):
    global cnt
    if s>N:
        return
    if s==N:
        cnt+=1
        if cnt==K:
            print('+'.join(map(str,arr)))
            exit(0)
    
    backtrack(s+1,arr+[1])
    backtrack(s+2,arr+[2])
    backtrack(s+3,arr+[3])

backtrack(0,[])
print(-1)
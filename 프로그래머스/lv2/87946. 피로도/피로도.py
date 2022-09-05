from itertools import permutations

def solution(k, dungeons):
    orders=permutations([i for i in range(len(dungeons))],len(dungeons))
    
    ans=0
    
    for order in orders:
        now=k
        cnt=0
        for n in order:
            if now>=dungeons[n][0]:
                now-=dungeons[n][1]
                cnt+=1
            else:
                ans=max(ans,cnt)
                break
        ans=max(ans,cnt)
    return ans
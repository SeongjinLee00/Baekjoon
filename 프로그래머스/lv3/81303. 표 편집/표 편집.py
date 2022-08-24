from collections import defaultdict

def solution(n, k, cmd):
    nums = defaultdict(lambda:[0,0,0]) # 이전, 다음
    deleted=[]
    for p in range(n):
        nums[p]=[p-1,p+1,p]
    for p in cmd:
        c=p[0]
        x=p[2:]
        if c=='U':
            for _ in range(int(x)):
                k=nums[k][0]
        elif c=='D':
            for _ in range(int(x)):
                k=nums[k][1]
        elif c=='C':
            nums[nums[k][0]][1]=nums[k][1]
            nums[nums[k][1]][0]=nums[k][0]
            deleted.append(nums[k])
            if nums[k][1]!=n:
                k=nums[k][1]
            else:
                k=nums[k][0]
        elif c=='Z':
            tmp=deleted.pop()
            nums[tmp[0]][1]=tmp[2]
            nums[tmp[1]][0]=tmp[2]
    ans=['O']*n
    for item in deleted:
        ans[item[2]]='X'
    
    return "".join(ans)
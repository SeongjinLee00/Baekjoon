s=input()
N=len(s)
answer='9'*1001
answer_score=-1

def check(s):
    if len(s)==2:
        if s[0]==s[1]:
            return 2
        else:
            return 0
    elif len(s)==3:
        if s[0]==s[1]==s[2]:
            return 2
        elif (s[0]==s[1]) or (s[1]==s[2]) or (s[0]==s[2]):
            return 1
        else:
            return 0
    return 0

dp=[-1]*(N+3)

def backtrack(now,k,candidate,score):
    global answer
    global answer_score

    if score<=dp[now]:
        return
    else:
        dp[now]=score
    if now==N:
        if score>answer_score:
            answer_score=score
            answer=candidate
        elif score==answer_score:
            if candidate<answer:
                answer=candidate
        return
    elif now>N:
        return

    backtrack(now+2,2,candidate+'-'+s[now:now+2],score+check(s[now:now+2]))
    backtrack(now+3,3,candidate+'-'+s[now:now+3],score+check(s[now:now+3]))

backtrack(2,2,s[0:2],check(s[0:2]))
backtrack(3,3,s[0:3],check(s[0:3]))
print(answer)
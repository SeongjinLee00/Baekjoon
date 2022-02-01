T=int(input())

scores=list(map(int,input().split()))

M=max(scores)

def whwkr(score):
    return score/M*100

scores=map(whwkr,scores)

print(sum(scores)/T)
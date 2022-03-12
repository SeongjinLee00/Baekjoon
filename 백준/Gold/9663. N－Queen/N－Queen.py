N=int(input())

queens=[]
ans=0
def backtrack():
    global ans

    if len(queens)==N:
        ans+=1
        return

    for c in range(N):
        is_Possible=1
        for i in range(len(queens)):
            if abs(len(queens)-i)==abs(c-queens[i]):
                is_Possible=0
                break
        
        if c not in queens and is_Possible:
            queens.append(c)
            backtrack()
            queens.pop()

backtrack()
print(ans)
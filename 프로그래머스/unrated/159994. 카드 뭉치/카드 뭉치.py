def solution(cards1, cards2, goal):
    l=0
    r=0
    
    while True:
        if l<len(cards1) and cards1[l]==goal[l+r]:
            l+=1
        elif r<len(cards2) and cards2[r]==goal[l+r]:
            r+=1
        else:
            return 'No'
        if l+r==len(goal):
            return 'Yes'
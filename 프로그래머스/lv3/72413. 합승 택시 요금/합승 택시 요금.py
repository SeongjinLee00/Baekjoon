def solution(n, s, a, b, fares):
    costs=[[float('inf')]*(n) for _ in range(n)]

    a-=1
    b-=1
    s-=1
    
    for p1,p2,cost in fares:
        costs[p1-1][p2-1]=cost
        costs[p2-1][p1-1]=cost

    for k in range(n):
        costs[k][k]=0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                costs[i][j]=min(costs[i][j], costs[i][k]+costs[k][j])

    ans=9999999999

    for k in range(n):
        if costs[s][k]+costs[k][a]+costs[k][b]<ans:
            ans=costs[s][k]+costs[k][a]+costs[k][b]

    return ans
from itertools import combinations

N=int(input())
table=[]

for _ in range(N):
    table.append(list(map(int,input().split())))

members=[i for i in range(N)]

selected_team=combinations(members,N//2)

min_difference=9999999999999
for team1 in selected_team:
    team2=[]
    for n in range(N):
        if n not in team1:
            team2.append(n)

    ability1=0
    ability2=0
    for i in range(len(team1)):
        for j in range(i+1,len(team1)):
            ability1+=table[team1[i]][team1[j]]
            ability1+=table[team1[j]][team1[i]]
            ability2+=table[team2[i]][team2[j]]
            ability2+=table[team2[j]][team2[i]]
    
    difference=abs(ability1-ability2)
    if difference<min_difference:
        min_difference=difference

print(min_difference)
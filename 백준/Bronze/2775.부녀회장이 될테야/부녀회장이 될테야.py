T=int(input())

people=[[0]*15 for _ in range(15)]

for _ in range(T):
    k=int(input())
    n=int(input())
    for i in range(15):
        people[0][i]=i

    for i in range(15):
        for j in range(1,15):
            people[j][i]=sum(people[j-1][0:i+1])

    print(people[k][n])
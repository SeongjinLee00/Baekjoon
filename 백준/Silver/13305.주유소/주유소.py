N=int(input())

roads=list(map(int,input().split()))
prices=list(map(int,input().split()))

money=0
oils=[0]

tempmin=prices[0]
for i in range(N-1):
    if tempmin>=prices[i+1]:
        tempmin=prices[i+1]
        oils.append(i+1)
if oils[-1]!=(N-1):
    oils.append(N-1)

distances=[]
for i in range(len(oils)-1):
    distances.append(sum(roads[oils[i]:oils[i+1]]))

oils.pop()
sum=0
for i in range(len(distances)):
    sum+=distances[i]*prices[oils[i]]

print(sum)
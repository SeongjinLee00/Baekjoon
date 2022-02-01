N=int(input())

pillars=[]
for _ in range(N):
    a,b=map(int,input().split())
    pillars.append([a,b])

for i in range(N):
    for j in range(N-1):
        if pillars[j][0]>pillars[j+1][0]:
            pillars[j+1],pillars[j]=pillars[j],pillars[j+1]

heights1=[0 for i in range(pillars[-1][0]+1)]
currheight=0

for i in range(len(heights1)):
    for j in range(len(pillars)):
        if i==pillars[j][0] and pillars[j][1]>currheight:
            currheight=pillars[j][1]
        heights1[i]=currheight

currheight=0
heights2=[0 for i in range(pillars[-1][0]+1)]
for i in list(range(len(heights2)))[::-1]:
    for j in list(range(len(pillars)))[::-1]:
        if i==pillars[j][0] and pillars[j][1]>currheight:
            currheight=pillars[j][1]
        heights2[i]=currheight

heights=list(map(min,heights1,heights2))

print(sum(heights))
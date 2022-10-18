from collections import defaultdict
import sys

input = sys.stdin.readline

N=int(input())

queries=[]

answers=[0]*N

colorsum=defaultdict(int)
for i in range(N):
    queries.append(list(map(int,input().split()))+[i])

queries.sort(key=lambda x:(x[1],x[0]))

cumul=0
j=0
for i in range(len(queries)):
    color, size, idx = queries[i][0], queries[i][1], queries[i][2]

    while queries[j][1]<size:
        colorsum[queries[j][0]]+=queries[j][1]
        cumul+=queries[j][1]
        j+=1

    answers[idx]=cumul-colorsum[color]
        
for i in range(N):
    print(answers[i])
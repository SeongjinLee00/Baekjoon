import sys

N,M=map(int,sys.stdin.readline().split())

dict1={}
for i in range(N):
    pokemon=sys.stdin.readline().rstrip()
    dict1[i]=(pokemon)

dict2={}
for key,value in dict1.items():
    dict2[value]=key

for _ in range(M):
    s=sys.stdin.readline().rstrip()
    if ord(s[0])<60:
        print(dict1[int(s)-1])
    else:
        print(dict2[s]+1)
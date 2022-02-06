import sys

N,M=map(int,sys.stdin.readline().split())

dict1={}
for _ in range(N):
    site, password=sys.stdin.readline().split()
    dict1[site]=(password)

for _ in range(M):
    s=sys.stdin.readline().rstrip()
    print(dict1[s])
import sys
input=sys.stdin.readline

S=input().rstrip()
N=len(S)

cnts=[[0]*N for _ in range(26)]

for i in range(N):
    cnts[ord(S[i])-97][i]+=1

for i in range(26):
    for j in range(1,N):
        cnts[i][j]+=cnts[i][j-1]

q=int(input())

for _ in range(q):
    s,l,r=input().split()
    l=int(l)
    r=int(r)

    n=ord(s)-97

    if l>=1: print(cnts[n][r]-cnts[n][l-1])
    if l==0: print(cnts[n][r])
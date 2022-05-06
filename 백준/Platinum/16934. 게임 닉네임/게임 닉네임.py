trie={}

def entrie(nickname):
    curr=trie
    depth=1
    first=True
    for ch in nickname:
        if ch not in curr:
            curr[ch]={}
            if first:
                print(nickname[0:depth])
                first=False
        curr=curr[ch]
        depth+=1
    if not curr.get('cnt'):
        curr['cnt']=1
        if first:
            print(nickname)
    else:
        if first:
            curr['cnt']+=1
            print(nickname+str(curr.get('cnt')))

N=int(input())

import sys
input=sys.stdin.readline

for _ in range(N):
    entrie(input().rstrip())
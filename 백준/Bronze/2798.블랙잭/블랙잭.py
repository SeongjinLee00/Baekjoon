N,M=map(int,input().split())

cards=list(map(int,input().split()))

max=0
for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            if cards[i]+cards[j]+cards[k]<=M and cards[i]+cards[j]+cards[k]>max and i!=j and j!=k and k!=i:
                max=cards[i]+cards[j]+cards[k]

print(max)
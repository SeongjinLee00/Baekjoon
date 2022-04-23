N,M=map(int,input().split())

parent=[0]*(N+1)

a,*truth=map(int,input().split())

if not truth:
    print(M)
    exit(0)

parties=[]

for _ in range(M):
    a,*member=map(int,input().split())

    parties.append(member)

for _ in range(50):
    for party in parties:
        flag=0
        for member in truth:
            if member in party:
                flag=1

        if flag:
            for member in party:
                if member not in truth:
                    truth.append(member)

cnt=0

for party in parties:
    flag=0
    for member in party:
        if member in truth:
            flag=1

    if not flag:
        cnt+=1

print(cnt)
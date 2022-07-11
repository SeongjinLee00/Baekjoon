N,M=map(int,input().split())

numbers=[]

for _ in range(N):
    s,e = map(int,input().split())

    if s>e:
        numbers.append([s,e])

if not numbers:
    print(M)
    exit(0)

numbers.sort(key=lambda x:x[1])
start=numbers[0][0]
end=numbers[0][1]

ans=0
for i in range(1,len(numbers)):
    if (numbers[i][0]>=start and numbers[i][1]<=start):
        start=numbers[i][0]
    
    elif (numbers[i][0]<=start and numbers[i][1]<=start):
        continue

    else:
        ans+=2*(start-end)
        start=numbers[i][0]
        end=numbers[i][1]

ans+=2*(start-end)
print(ans+M)
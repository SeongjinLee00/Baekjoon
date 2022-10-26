N=int(input())
K=int(input())
numbers=sorted(list(map(int,input().split())))

if N==1:
    print(0)
    exit(0)
distances=[]

for i in range(N-1):
    distances.append(numbers[i+1]-numbers[i])

distances.sort()

for _ in range(K-1):
    distances.pop()

print(sum(distances))
N=int(input())

numbers=list(map(int,input().split()))

candidates=[numbers[0]]

for i in range(N-1):
    candidates.append(max(candidates[i]+numbers[i+1],numbers[i+1]))

print(max(candidates))
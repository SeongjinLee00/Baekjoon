N=int(input())

for i in range(26):
    for j in range(2,N+1):
        if N%j==0:
            print(j)
            N=N//j
            break
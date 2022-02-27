N,M=map(int,input().split())

distances=[]

for _ in range(N):
    distances.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            distances[i][j]=min(distances[i][j],distances[i][k]+distances[k][j])

for _ in range(M):
    A,B,C=map(int,input().split())

    if distances[A-1][B-1]>C:
        print('Stay here')
    else:
        print('Enjoy other party')
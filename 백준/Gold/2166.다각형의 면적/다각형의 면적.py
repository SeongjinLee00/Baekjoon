N=int(input())

points=[]
sum=0
for _ in range(N):
    temp=list(map(int,input().split()))
    points.append(temp)

for i in range(N-1):
    sum = sum + points[i][0]*points[i+1][1]-points[i+1][0]*points[i][1]

sum=sum+points[N-1][0]*points[0][1]-points[0][0]*points[N-1][1]

print(0.5*abs(sum))
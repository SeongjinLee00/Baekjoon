points=[]

for _ in range(3):
    temp=list(map(int,input().split()))
    points.append(temp)

vector1=[points[1][0]-points[0][0],points[1][1]-points[0][1]]
vector2=[points[2][0]-points[1][0],points[2][1]-points[1][1]]

crossproduct=vector1[0]*vector2[1]-vector2[0]*vector1[1]

if crossproduct>0:
    print(1)
elif crossproduct<0:
    print(-1)
elif crossproduct==0:
    print(0)
from itertools import permutations

numbersss=list(map(int,input().split()))

def cross(q1,q2,q3):
    p1=[q2[0]-q1[0],q2[1]-q1[1]]
    p2=[q3[0]-q2[0],q3[1]-q2[1]]
    if p1[0]*p2[1]-p1[1]*p2[0]<0.0001:
        return 1
    else:
        return -1

numberss=permutations(numbersss,8)

ans=0
for numbers in numberss:
    coordinates=[[0,numbers[0]],[0.7071*numbers[1],0.7071*numbers[1]],[numbers[2],0],[0.7071*numbers[3],-0.7071*numbers[3]],[0,-numbers[4]],[-0.7071*numbers[5],-0.7071*numbers[5]],[-numbers[6],0],[-0.7071*numbers[7],0.7071*numbers[7]]]
    if cross(coordinates[0],coordinates[1],coordinates[2])+cross(coordinates[1],coordinates[2],coordinates[3])+cross(coordinates[2],coordinates[3],coordinates[4])+cross(coordinates[3],coordinates[4],coordinates[5])+cross(coordinates[4],coordinates[5],coordinates[6])+cross(coordinates[5],coordinates[6],coordinates[7])+cross(coordinates[6],coordinates[7],coordinates[0])+cross(coordinates[7],coordinates[0],coordinates[1])==8:
        ans+=1

print(ans)
import math

N, maxnumber=map(int,input().split())

rooms=0
students=[]
for _ in range(N):
    a,b=map(int,input().split())
    students.append([a,b])

rooms += math.ceil(students.count([0,1])/maxnumber)
rooms += math.ceil(students.count([0,2])/maxnumber)
rooms += math.ceil(students.count([0,3])/maxnumber)
rooms += math.ceil(students.count([0,4])/maxnumber)
rooms += math.ceil(students.count([0,5])/maxnumber)
rooms += math.ceil(students.count([0,6])/maxnumber)
rooms += math.ceil(students.count([1,1])/maxnumber)
rooms += math.ceil(students.count([1,2])/maxnumber)
rooms += math.ceil(students.count([1,3])/maxnumber)
rooms += math.ceil(students.count([1,4])/maxnumber)
rooms += math.ceil(students.count([1,5])/maxnumber)
rooms += math.ceil(students.count([1,6])/maxnumber)

print(rooms)
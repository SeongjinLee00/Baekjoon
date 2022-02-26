x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

vector1=[x2-x1,y2-y1]
vector2=[x3-x2,y3-y2]
vector3=[x4-x2,y4-y2]

vector4=[x4-x3,y4-y3]
vector5=[x1-x4,y1-y4]
vector6=[x2-x4,y2-y4]

def is_CCW(vec1,vec2):
    if vec1[0]*vec2[1]-vec2[0]*vec1[1]>0:
        return 1
    else :
        return -1

if is_CCW(vector1,vector2)*is_CCW(vector1,vector3)==-1 and is_CCW(vector4,vector5)*is_CCW(vector4,vector6)==-1:
    print(1)
else:
    print(0)
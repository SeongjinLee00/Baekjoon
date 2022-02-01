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

def is_inside(a,b,c):
    if a<=c:
        if a<=b<=c:
            return True
        else:
            return False
    if a>=c:
        if a>=b>=c:
            return True
        else:
            return False

a=[x4-x1,y4-y1][0]*[x2-x4,y2-y4][1]-[x4-x1,y4-y1][1]*[x2-x4,y2-y4][0]
b=[x3-x1,y3-y1][0]*[x2-x3,y2-y3][1]-[x3-x1,y3-y1][1]*[x2-x3,y2-y3][0]
c=[x1-x3,y1-y3][0]*[x4-x1,y4-y1][1]-[x1-x3,y1-y3][1]*[x4-x1,y4-y1][0]
d=[x2-x3,y2-y3][0]*[x4-x2,y4-y2][1]-[x2-x3,y2-y3][1]*[x4-x2,y4-y2][0]

if [x1,y1]==[x3,y3] or [x1,y1]==[x4,y4] or [x2,y2]==[x3,y3] or [x2,y2]==[x4,y4]:
    print(1)

elif (a==0 and is_inside(x1,x4,x2) and is_inside(y1,y4,y2)) or (b==0 and is_inside(x1,x3,x2) and is_inside(y1,y3,y2)) or (c==0 and is_inside(x3,x1,x4) and is_inside(y3,y1,y4)) or (d==0 and is_inside(x3,x2,x4) and is_inside(y3,y2,y4)):
    print(1)

else:

    if is_CCW(vector1,vector2)*is_CCW(vector1,vector3)==-1 and is_CCW(vector4,vector5)*is_CCW(vector4,vector6)==-1:
        print(1)
    else:
        print(0)
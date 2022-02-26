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

def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    intersection_x=0
    intersection_y=0

    if x1==x2==x3==x4: # 모두 기울기 무한이면
        if (abs(max(x1,x2,x3,x4)-min(x1,x2,x3,x4))==abs(x2-x1)+abs(x4-x3)) and (abs(max(y1,y2,y3,y4)-min(y1,y2,y3,y4))==abs(y2-y1)+abs(y4-y3)) : #한 점에서 만나는 특별한 경우
            if [x1,y1]==[x3,y3] or [x1,y1]==[x4,y4]:
                print(x1,y1)
            elif [x2,y2]==[x3,y3] or [x2,y2]==[x4,y4]:
                print(x2,y2)
        else :
            pass
    elif x1==x2: # 1번직선 기울기 무한이면
        m2=(y4-y3)/(x4-x3)
        intersection_x=x1
        intersection_y=m2*(x1-x3)+y3

        print(intersection_x, intersection_y)
    elif x3==x4: # 2번직선 기울기 무한이면
        m1=(y2-y1)/(x2-x1)       
        intersection_x=x3
        intersection_y=m1*(x3-x1)+y1 
        print(intersection_x, intersection_y)
    elif ((y2-y1)/(x2-x1))==((y4-y3)/(x4-x3)): # 평행하면
        if (abs(max(x1,x2,x3,x4)-min(x1,x2,x3,x4))==abs(x2-x1)+abs(x4-x3)) and (abs(max(y1,y2,y3,y4)-min(y1,y2,y3,y4))==abs(y2-y1)+abs(y4-y3)) : #한 점에서 만나는 특별한 경우
            if [x1,y1]==[x3,y3] or [x1,y1]==[x4,y4]:
                print(x1,y1)
            elif [x2,y2]==[x3,y3] or [x2,y2]==[x4,y4]:
                print(x2,y2)
        else :
            pass
    else: # 일반적인 경우
        m1=(y2-y1)/(x2-x1)
        m2=(y4-y3)/(x4-x3)
        d1=y1-m1*x1
        d2=y3-m2*x3
        intersection_x=(d2-d1)/(m1-m2)
        intersection_y=((d2-d1)/(m1-m2))*m1+d1
        print(intersection_x,intersection_y)


a=[x4-x1,y4-y1][0]*[x2-x4,y2-y4][1]-[x4-x1,y4-y1][1]*[x2-x4,y2-y4][0]
b=[x3-x1,y3-y1][0]*[x2-x3,y2-y3][1]-[x3-x1,y3-y1][1]*[x2-x3,y2-y3][0]
c=[x1-x3,y1-y3][0]*[x4-x1,y4-y1][1]-[x1-x3,y1-y3][1]*[x4-x1,y4-y1][0]
d=[x2-x3,y2-y3][0]*[x4-x2,y4-y2][1]-[x2-x3,y2-y3][1]*[x4-x2,y4-y2][0]

if [x1,y1]==[x3,y3] or [x1,y1]==[x4,y4] or [x2,y2]==[x3,y3] or [x2,y2]==[x4,y4]: # 한 점에서 만나는 경우
    print(1)
    intersection(x1,y1,x2,y2,x3,y3,x4,y4)

# 일직선 상에 있는 경우
elif (a==0 and is_inside(x1,x4,x2) and is_inside(y1,y4,y2)) or (b==0 and is_inside(x1,x3,x2) and is_inside(y1,y3,y2)) or (c==0 and is_inside(x3,x1,x4) and is_inside(y3,y1,y4)) or (d==0 and is_inside(x3,x2,x4) and is_inside(y3,y2,y4)):
    print(1)
    intersection(x1,y1,x2,y2,x3,y3,x4,y4)

else:
# 일반적인 경우
    if is_CCW(vector1,vector2)*is_CCW(vector1,vector3)==-1 and is_CCW(vector4,vector5)*is_CCW(vector4,vector6)==-1:
        print(1)
        intersection(x1,y1,x2,y2,x3,y3,x4,y4)
    else:
        print(0)
w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())

# dir=[1,1] # 맨 처음에 생각한 방법, 답은 나오겠지만 시간초과입니다

# while t!=0:
#     p=p+dir[0]
#     q=q+dir[1]
#     t=t-1

#     if p==w:
#         dir[0]=-1
#     if q==h:
#         dir[1]=-1
#     if p==0:
#         dir[0]=1
#     if q==0:
#         dir[1]=1

p=(p+(t%(2*w)))%(2*w)
if p>w:
    p=2*w-p
q=(q+(t%(2*h)))%(2*h)
if q>h:
    q=2*h-q

print(p,q)
w,h=map(int,input().split())
N=int(input())
perimeter=2*(w+h)
positions=[]
for _ in range(N):
    dir, pos=map(int,input().split())

    if dir==1:
        positions.append(-pos)
    if dir==4:
        positions.append(-w-pos)
    if dir==3:
        positions.append(pos)
    if dir==2:
        positions.append(h+pos)

currposition=0
currdir, currpos=map(int,input().split())

if currdir==1:
    currposition=(-currpos)
if currdir==4:
    currposition=(-w-currpos)
if currdir==3:
    currposition=currpos
if currdir==2:
    currposition=(currpos+h)

length=[]
for i in range(N):
    length.append(min(abs(currposition-positions[i]),perimeter-abs(currposition-positions[i])))

print(sum(length))
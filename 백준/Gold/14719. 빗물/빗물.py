H,W=map(int,input().split())
heights=list(map(int,input().split()))
left=[0]*W
right=[0]*W

M=0
for i in range(W):
    M=max(M,heights[i])
    left[i]=M

M=0
for i in range(W-1,-1,-1):
    M=max(M,heights[i])
    right[i]=M

ans=0

for i in range(W):
    ans+=min(left[i],right[i])-heights[i]

print(ans)
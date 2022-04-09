# T T T T T F F F F F
def check(num): # 모든 섬 사이의 거리가 적어도 num 이상이 되게 하는것이 가능한지 확인하는 함수
    curr_loc=0
    cnt=0

    for i in range(len(numbers)):
        if numbers[i]-curr_loc<num:
            cnt+=1
            if cnt>m:
                return False
        else:
            curr_loc=numbers[i]

    return True

d,n,m=map(int,input().split())
import sys
if n==0:
    print(d)
    exit(0)

numbers=[]

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

start=0
end=10**10

while start+1<end:
    mid=(start+end)//2
    if check(mid):
        start=mid
    else:
        end=mid

print(start)
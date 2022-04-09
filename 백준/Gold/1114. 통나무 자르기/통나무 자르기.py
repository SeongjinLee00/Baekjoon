L,K,C=map(int,input().split())

numbers=list(map(int,input().split()))
numbers_=list(set(numbers))
numbers_.sort()
# 가장 긴 조각의 최솟값을 구하자
# F F F F F T T T T T
numbers_=numbers_+[L]
ans={}
def check(num): # 모든 조각이 num보다 작거나 같게 하는것이 가능한지 확인하는 함수
    cnt=0
    curr_pos=0

    if num>=L:
        return True

    if num>=numbers_[-1]:
        if L-numbers[-1]<=num:
            return True

    for i in range(len(numbers_)-1):

        if numbers_[i]-curr_pos<=num and numbers_[i+1]-curr_pos>num:
            cnt+=1
            curr_pos=numbers_[i]
            if cnt>C:
                return False
    
    last=L-curr_pos

    if last<=num:
        return True

start=0
end=10**10

while start+1<end:
    mid=(start+end)//2
    if check(mid):
        end=mid
    else:
        start=mid

print(end,end=' ')

cut=[]
num=end
curr_pos=0

if num>=L:
    cut.append(numbers_[0])

if num>=numbers_[-1]:
    for i in range(len(numbers_)):
        if L-numbers_[i]<=num and numbers_[i]<=num:
            cut.append(numbers_[i])
            break

for i in range(len(numbers_)-1):
    if numbers_[i]-curr_pos<=num and numbers_[i+1]-curr_pos>num:
        cut.append(numbers_[i])
        curr_pos=numbers_[i]

cut_=[]

for i in range(len(cut)):
    if L-cut[i] in numbers_:
        cut_.append(L-cut[i])

cut_.sort()

flag=0
if len(cut)<C:
    print(numbers_[0])
    exit(0)
if len(cut)==len(cut_):
    print(min(cut[0],cut_[0]))
    exit(0)

cut=[]
curr_pos=L
for i in range(len(numbers_)-1,0,-1):
    if curr_pos-numbers_[i]<=num and curr_pos-numbers_[i-1]>num:
        cut.append(numbers_[i])
        curr_pos=numbers_[i]

if cut:
    print(cut[-1])
else:
    print(numbers_[0])
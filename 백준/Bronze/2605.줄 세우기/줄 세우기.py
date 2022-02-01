N=int(input())
cards=list(map(int,input().split()))

students=[]

for i in range(1,N+1):
    students.append(i)

def swap(i,card):
    if card==0:
        pass
    else:
        for k in range(card):
            students[i-k-1],students[i-k-2]=students[i-k-2],students[i-k-1]

for j in range(N):
    swap(students[j],cards[j])

for str in students:
    print(str,end=' ')
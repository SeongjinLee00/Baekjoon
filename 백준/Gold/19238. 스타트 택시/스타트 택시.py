from collections import deque

N,M,fuel=map(int,input().split())
customer=M
area=[]
for _ in range(N):
    area.append(list(map(int,input().split())))

curr_r, curr_c=map(int,input().split())
curr_r-=1
curr_c-=1

destinations={}
for _ in range(M):
    a,b,c,d=map(int,input().split())
    area[a-1][b-1]=2
    destinations[(a-1,b-1)]=(c-1,d-1)
dr=[1,-1,0,0]
dc=[0,0,1,-1]

customers=[]
def to_customer(r,c):
    global fuel
    global curr_r
    global curr_c
    global customers
    flag=0
    customers=[]
    q=deque([[r,c,0]])
    visited=[[0]*N for _ in range(N)]
    while q:
        r,c,d=q.popleft()
        if area[r][c]==2:
            curr_r=r
            curr_c=c
            fuel=fuel
            customers.append([r,c,d])
            return

        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area[rr][cc]!=1 and not visited[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
                if area[rr][cc]==2:
                    flag=1
                    customers.append([rr,cc,d+1])
    if flag==0:
        print(-1)
        exit(0)

def to_destination(r,c):
    global customer
    global fuel
    global curr_r
    global curr_c
    flag=0
    q=deque([[r,c,0]])
    visited=[[0]*N for _ in range(N)]
    destination=destinations[(curr_r,curr_c)]
    while q:
        r,c,d=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and area[rr][cc]!=1 and not visited[rr][cc]:
                visited[rr][cc]=1
                q.append([rr,cc,d+1])
                if (rr,cc)==destination:
                    flag=1
                    fuel-=(d+1)
                    if fuel>=0:
                        curr_r=rr
                        curr_c=cc
                        customer-=1
                        fuel+=2*(d+1)
                        if customer==0:
                            print(fuel)
                            exit(0)
                        else:
                            return 0
                    else:
                        print(-1)
                        exit(0)
    if flag==0:
        print(-1)
        exit(0)

while True:
    to_customer(curr_r,curr_c)

    customers.sort(key=lambda x:(x[2],x[0],x[1]))

    fuel-=(customers[0][2])

    if fuel>=0:
        curr_r=customers[0][0]
        curr_c=customers[0][1]
        area[curr_r][curr_c]=0
    else:
        print(-1)
        exit(0)

    to_destination(curr_r,curr_c)
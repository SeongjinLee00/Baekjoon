R,C,ZR,ZC=map(int,input().split())

board=[]

for _ in range(R):
    board.append(input())

for row in board:
    for _ in range(ZR):
        for c in row:
            print(c*ZC,end='')
        print()
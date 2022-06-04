def move(howmany, start, end, remainder):
    if howmany==1:
        print(start, end)
        return
    else:
        move(howmany-1, start, remainder, end)
        move(1, start, end, remainder)
        move(howmany-1, remainder, end, start)
N=int(input())
print(2**N-1)
move(N,1,3,2)
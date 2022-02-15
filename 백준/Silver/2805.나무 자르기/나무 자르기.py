N,M=map(int,input().split())

trees=list(map(int,input().split()))

start=0
end=max(trees)

while start<=end: # start가 더 커져야 탈출
    cut=(start+end)//2 
    harvest=sum([max(x-cut,0) for x in trees])
    if harvest<M:
        end=cut-1
    elif harvest>M:
        start=cut+1
    else:
        break

if harvest==M:
    print(cut)
else:
    for i in range(2):
        harvest=sum([max(x-(cut+i),0) for x in trees])
        if harvest>=M:
            continue
        if harvest<M:
            cut=cut+i-1
            break

    print(cut)

K,N=map(int,input().split())

wires=[]

for _ in range(K):
    wires.append(int(input()))

start=1
end=max(wires)

while start<=end:
    cut=(start+end)//2
    get=sum([length//cut for length in wires])

    if get>=N:
        start=cut+1
    elif get<N:
        end=cut-1

for k in range(2,-3,-1):
    if sum([length//(cut+k) for length in wires])>=N:
        print(cut+k)
        break
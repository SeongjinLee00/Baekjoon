N,M=map(int,input().split())

hear=set()
see=[]

for _ in range(N):
    hear.add(input())

for _ in range(M):
    see.append(input())

hearsee=[]

for name in see:
    if name in hear:
        hearsee.append(name)

hearsee.sort()

print(len(hearsee))
for name in hearsee:
    print(name)
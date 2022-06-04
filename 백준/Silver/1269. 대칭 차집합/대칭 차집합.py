N,M=map(int,input().split())

A=set(map(int,input().split()))
B=set(map(int,input().split()))

cross=0
for number in A:
    if number in B:
        cross+=1

print(len(A)+len(B)-2*cross)
N=int(input())

sequence=list(map(int,input().split()))

if N==1:
    print(1)
elif N==2:
    print(2)
else:
    def LIS(lst):
        i=0
        maxlen=1
        len=1
        while True:
            if lst[i]<=lst[i+1]:
                len = len+1
            else:
                len=1

            if maxlen<len:
                maxlen=len
            i=i+1

            if i==N-1:
                return maxlen

    def LDS(lst):
        i=0
        maxlen=1
        len=1
        while True:
            if lst[i]>=lst[i+1]:
                len = len+1
            else:
                len=1

            if maxlen<len:
                maxlen=len
            i=i+1

            if i==N-1:
                return maxlen    

    print(max(LIS(sequence),LDS(sequence)))
import copy

T=int(input())

for _ in range(T):
    signal=list(input())
    signal_write=copy.deepcopy(signal)
    for _ in range(50):
        for i in range(1,len(signal)-1):
            if i>=2:
                if signal[i]=='0' and signal[i+1]=='0' and (signal[i-1]=='1' and signal[i-2]=='1'):

                    j=i+1
                    while signal[j]=='0':
                        j=j+1
                        if j==len(signal):
                            break
                        else:
                            k=j
                            while signal[k]=='1':
                                k=k+1
                                if k==len(signal):
                                    break

                            for l in range(i-1,k):
                                signal_write[l]='x'
            else:
                if signal[i]=='0' and signal[i+1]=='0' and signal[i-1]=='1':

                    j=i+1
                    while signal[j]=='0':
                        j=j+1
                        if j==len(signal):
                            break
                        else:
                            k=j
                            while signal[k]=='1':
                                k=k+1
                                if k==len(signal):
                                    break

                            for l in range(i-1,k):
                                signal_write[l]='x'

    for _ in range(100):
        for m in range(1,len(signal)):
            if signal[m-1]=='0' and signal[m]=='1':
                signal_write[m-1]='x'
                signal_write[m]='x'

    if signal_write.count('0')==0 and signal_write.count('1')==0:
        print('YES')
    else:
        print('NO')
T=int(input())

for t in range(T):
    ttt,tth,tht,thh,htt,hth,hht,hhh=0,0,0,0,0,0,0,0
    s=input()
    for i in range(38):
        if s[i:i+3]=='TTT':
            ttt+=1
        elif s[i:i+3]=='TTH':
            tth+=1
        elif s[i:i+3]=='THT':
            tht+=1
        elif s[i:i+3]=='THH':
            thh+=1
        elif s[i:i+3]=='HTT':
            htt+=1
        elif s[i:i+3]=='HTH':
            hth+=1
        elif s[i:i+3]=='HHT':
            hht+=1
        elif s[i:i+3]=='HHH':
            hhh+=1
        else:
            raise Exception

    print(ttt,tth,tht,thh,htt,hth,hht,hhh)
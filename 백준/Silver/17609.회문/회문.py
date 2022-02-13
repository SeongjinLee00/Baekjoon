N=int(input())

for _ in range(N):
    s=input()
    i=0
    ID=0
    j=len(s)-1
    ID_S=[0,0]
    indicator=0
    while i<=j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            if s[i+1]==s[j] and s[i]==s[j-1]: # 특이케이스
                a=i
                b=j
                if indicator==0:
                    i+=1
                    ID_S[0]+=1
                    indicator+=1
                    while i<=j:
                        if s[i]==s[j]:
                            i+=1
                            j-=1
                        else:
                            if s[i+1]==s[j]:
                                i+=1
                                ID_S[0]+=1
                            elif s[i]==s[j-1]:
                                j-=1
                                ID_S[0]+=1
                            else:
                                ID_S[0]+=2
                                break
                i=a
                j=b
                if indicator==1:
                    j-=1
                    ID_S[1]+=1
                    while i<=j:
                        if s[i]==s[j]:
                            i+=1
                            j-=1
                        else:
                            if s[i+1]==s[j]:
                                i+=1
                                ID_S[1]+=1
                            elif s[i]==s[j-1]:
                                j-=1
                                ID_S[1]+=1
                            else:
                                ID_S[1]+=2
                                break
            if indicator==1:
                break
            elif s[i+1]==s[j]:
                i+=1
                ID+=1
            elif s[i]==s[j-1]:
                j-=1
                ID+=1
            else:
                ID+=2
                break

    if indicator!=0:
        if min(ID_S)+ID>=3:
            print(2)
        else:
            print(min(ID_S)+ID)
    else:
        if ID>=3:
            print(2)
        else:
            print(ID)
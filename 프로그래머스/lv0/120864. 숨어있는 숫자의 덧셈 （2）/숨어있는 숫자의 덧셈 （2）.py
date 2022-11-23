def solution(my_string):
    tmp=''
    
    ans=0
    i=0
    while True:
        while my_string[i].isnumeric():
            tmp+=my_string[i]
            i+=1
            if i==len(my_string):
                break

        if tmp:
            ans+=int(tmp)
            tmp=''
        i+=1
        if i>=len(my_string):
            break
    return ans
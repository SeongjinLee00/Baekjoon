def solution(numbers):
    d={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    tmp=''
    ret=''
    i=0
    while True:
        tmp+=numbers[i]
        if tmp in d:
            ret+=d[tmp]
            tmp=''
        
        i+=1
        if i==len(numbers):
            return int(ret)
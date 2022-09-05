def solution(array, commands):
    ret=[]
    for s,e,k in commands:
        ret.append(sorted(array[s-1:e])[k-1])
    return ret
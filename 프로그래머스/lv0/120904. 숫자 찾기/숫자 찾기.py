def solution(num, k):
    num=str(num)
    for i in range(len(num)):
        if num[i]==str(k):
            return i+1
    return -1
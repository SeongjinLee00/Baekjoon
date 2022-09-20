def solution(left, right):
    s=set()
    for i in range(1,33):
        s.add(i*i)
    ans=0
    for number in range(left,right+1):
        if number in s:
            ans-=number
        else:
            ans+=number

    return ans
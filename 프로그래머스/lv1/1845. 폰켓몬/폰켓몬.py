def solution(nums):
    s=set()
    for n in nums:
        s.add(n)
    return min(len(s),len(nums)//2)
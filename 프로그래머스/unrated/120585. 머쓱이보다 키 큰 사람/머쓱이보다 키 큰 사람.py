def solution(array, height):
    array.sort()
    
    from bisect import bisect_right
    
    return len(array)-bisect_right(array,height)
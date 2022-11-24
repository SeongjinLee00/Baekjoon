def solution(num, total):
    for x in range(-100,100):
        if 2*total==num*(2*x+(num-1)):
            return [x+i for i in range(num)]
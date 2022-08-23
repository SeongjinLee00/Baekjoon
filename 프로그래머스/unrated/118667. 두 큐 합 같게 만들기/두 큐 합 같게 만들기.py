def solution(queue1, queue2):
    que = queue1 + queue2
    n = len(queue1)
    total = sum(que)
    if total % 2:
        return -1
    s = 0
    e = n - 1
    ans = 0
    my_sum = sum(queue1)
    target = total // 2
    while s <= e < 2 * n:
        if my_sum < target:
            e += 1
            ans += 1
            if e == 2 * n:
                return -1
            my_sum += que[e]
        elif my_sum > target:
            my_sum -= que[s]
            s += 1
            ans += 1
        else:
            return ans
    return -1
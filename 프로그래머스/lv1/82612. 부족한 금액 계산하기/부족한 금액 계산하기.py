def solution(price, money, count):
    total=count*(price+price*count)//2
    
    return max(total-money,0)
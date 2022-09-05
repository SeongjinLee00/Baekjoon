from datetime import date
def solution(a, b):
    d={0:"MON", 1:"TUE", 2:"WED", 3:"THU", 4:"FRI", 5:"SAT", 6:"SUN"}
    return d[date(2016,a,b).weekday()]
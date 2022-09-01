def solution(sizes):
    xx=0
    yy=0
    for x,y in sizes:
        if y>x:
            x,y=y,x
        if x>xx:
            xx=x
        if y>yy:
            yy=y
    return xx*yy
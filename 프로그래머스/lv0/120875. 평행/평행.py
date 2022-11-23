def solution(dots):
    for i in range(4):
        for j in range(4):
            if i==j:
                continue
                
            tmp=[0,1,2,3]
            tmp.remove(i)
            tmp.remove(j)
            k=tmp[0]
            l=tmp[1]
            
            if (dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0])==(dots[k][1]-dots[l][1])/(dots[k][0]-dots[l][0]) or (dots[i][1]-dots[j][1])/(dots[i][0]-dots[j][0])==(dots[l][1]-dots[k][1])/(dots[l][0]-dots[k][0]):
                return 1
    return 0
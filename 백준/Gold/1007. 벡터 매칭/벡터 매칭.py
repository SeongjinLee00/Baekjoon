from itertools import combinations

T=int(input())

for t in range(T):
    N=int(input())

    points=[]

    for _ in range(N):
        points.append(list(map(int,input().split())))

    x_sum=0
    y_sum=0
    for x,y in points:
        x_sum+=x
        y_sum+=y

    starts=combinations(points,N//2)

    ans=999999999999999

    for start in starts:
        x_sum_start=0
        y_sum_start=0
        for x,y in start:
            x_sum_start+=x
            y_sum_start+=y

        x_sum_end=x_sum-x_sum_start
        y_sum_end=y_sum-y_sum_start

        vector_x=x_sum_start-x_sum_end
        vector_y=y_sum_start-y_sum_end

        norm=(abs(vector_x)**2+abs(vector_y)**2)**0.5

        if norm<ans:
            ans=norm

    print(ans)
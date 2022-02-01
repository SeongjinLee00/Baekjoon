T=int(input())

for _ in range(T):
    scores=list(map(int,input().split()))

    students_num=scores[0]
    scores.remove(students_num)

    average=sum(scores)/students_num

    count=0
    for i in range(len(scores)):
        if scores[i]>average:
            count=count+1

    print('%.3f' %(count/students_num*100)+'%')
from math import ceil
from collections import defaultdict


def solution(fees, records):
    d1=dict()
    d2=defaultdict(int)
    
    def cal(mins):
        if int(mins)<=fees[0]:
            return fees[1]
        else:
            return fees[1]+ceil((int(mins)-fees[0])/fees[2])*fees[3]    
    
    for record in records:
        time, number, io = record.split()
        time = int(time[0]+time[1])*60+int(time[3]+time[4])
        
        if number in d1:
            t1=d1.pop(number)
            d2[number]+=(time-t1)
        else:
            d1[number]=time
            
    for k,v in d1.items():
        d2[k]+=(1439-v)
    
    ret=[]
    for k,v in sorted(d2.items()):
        ret.append(cal(v))
    
    return ret
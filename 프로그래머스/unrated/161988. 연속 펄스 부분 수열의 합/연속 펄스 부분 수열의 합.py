def solution(sequence):
    sequence1=[0]*len(sequence)
    sequence2=[0]*len(sequence)
    
    for i in range(len(sequence)):
        if i%2:
            sequence1[i]=sequence[i]
            sequence2[i]=-sequence[i]
        else:
            sequence1[i]=-sequence[i]
            sequence2[i]=sequence[i]
    
    for i in range(1,len(sequence)):
        sequence1[i]+=sequence1[i-1]
        sequence2[i]+=sequence2[i-1]
    
    sequence1=[0]+sequence1
    return max(sequence1)-min(sequence1)
def solution(sequence, k):
    answer = []
    start, end = 0, 1
    sum_num=sequence[start]
    
    while start<end:
        if sum_num == k:
            if answer:
                answer= [start, end-1] if answer[1]-answer[0]>end-1-start else answer
            else:
                answer=[start, end-1]
            sum_num-=sequence[start]
            start+=1
            if end+1<=len(sequence):
                end+=1
                sum_num+=sequence[end-1]
        elif sum_num<k:
            if end == len(sequence):
                sum_num-=sequence[start]
                start+=1 
            elif end+1<=len(sequence):
                end+=1
                sum_num+=sequence[end-1]
        elif sum_num>k:
            sum_num-=sequence[start]
            start+=1
    return answer
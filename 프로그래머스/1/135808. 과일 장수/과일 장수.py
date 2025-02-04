def solution(k, m, score):
    answer = 0
    score=sorted(score, reverse=True)
    
    score=[score[i:i+m] for i in range(0, len(score), m)]
    
    for box in score:
        if len(box)<m:
            continue
        else:
            answer+=box[-1]*m
        
    return answer
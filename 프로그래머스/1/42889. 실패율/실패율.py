def solution(N, stages):
    answer = {i+1:0 for i in range(N)}
    
    right=len(stages)
    left=0
    
    for i in range(1,N+1):
        left=len([s for s in stages if s==i])
        fail=(left/right) if left else 0
        answer[i]=fail
        
        right-=left
    
    answer = [k for k,v in sorted(answer.items(), key=lambda x: (-x[1], int(x[0])))]
    return answer 
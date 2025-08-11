def solution(elements):
    answer = []
    length=len(elements)
    
    for i in range(length):
        sub = elements+elements[:i]
        for j in range(1, length+1):
            answer.append(sum(sub[i:i+j]))
    
    answer=len(list(set(answer)))
    return answer
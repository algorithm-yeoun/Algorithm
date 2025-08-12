def solution(clothes):
    answer = {}
    for clothing in clothes:
        if clothing[1] in answer:
            answer[clothing[1]]+=1
        else:
            answer[clothing[1]]=2
    
    result=1
    for i in answer.values():
        result*=i
    
    return result-1
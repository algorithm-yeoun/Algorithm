def solution(data, ext, val_ext, sort_by):
    answer = []
    standard = {"code":0, "date":1, "maximum":2, "remain":3}
    
    for d in data:
        if d[standard[ext]]<val_ext:
            answer.append(d)
    
    answer=sorted(answer, key=lambda x: x[standard[sort_by]])
    
    return answer
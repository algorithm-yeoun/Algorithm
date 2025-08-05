def solution(keymap, targets):
    answer = []
    unique_keys="".join(set("".join(keymap)))
    
    for t in targets:
        result=0
        for i in t:
            min_n=1000
            if i in unique_keys:
                for k in keymap:
                    if k.find(i)>=0:
                        min_n = min(k.find(i)+1, min_n)
                result+=min_n    
            else:
                result=-1
                break
        answer.append(result)
    return answer
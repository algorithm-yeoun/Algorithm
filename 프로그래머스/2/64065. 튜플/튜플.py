def solution(s):
    s = s[2:-2]
    parts = s.split("},{")
    lists = [list(map(int, p.split(","))) for p in parts]
    s_list = sorted(lists, key=len)

    answer = []
    
    for i in range(len(s_list)):
        for j in answer:
            if j in s_list[i]:
                s_list[i].remove(j)
        else:
            answer.append(s_list[i][-1])
        
    return answer
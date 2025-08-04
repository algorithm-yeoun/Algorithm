def solution(babbling):
    bab=["aya","ye","woo","ma"]
    for i in range(len(babbling)):
        for j in range(len(bab)):
            babbling[i]=babbling[i].replace(bab[j], str(j))
    answer=0
    for i in babbling:
        if i.isdigit():
            for x in range(1, len(i)):
                if i[x]==i[x-1]:
                    break;
            else:
                answer+=1        
    return answer
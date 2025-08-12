def solution(progresses, speeds):
    answer = []
    cnt_day=[]
    
    for i in range(len(progresses)):
        div_n=1 if (100-progresses[i])%speeds[i] else 0
        cnt_day.append((100-progresses[i])//speeds[i] + div_n)
    
    temp=cnt_day[0]
    cnt=1
    
    for i in cnt_day[1:]:
        if temp<i:
            answer.append(cnt)
            cnt=1
            temp=i
        else:
            cnt+=1
    else:
        answer.append(cnt)

    
    return answer
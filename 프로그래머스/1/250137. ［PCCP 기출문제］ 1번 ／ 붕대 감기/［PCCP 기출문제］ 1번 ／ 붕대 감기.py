def solution(bandage, health, attacks):
    answer, cnt = 0, 0
    t, x, y = bandage[0], bandage[1], bandage[2]
    max_time = attacks[-1]
    max_time = max_time[0]
    attack= {i[0]:i[1] for i in attacks}
    cur_health = health
    
    for i in range(1, max_time+1):
        if i in attack.keys():
            cur_health-=attack[i]
            cnt=0
        else:
            cnt+=1
            if cnt==t:
                cnt=0
                cur_health+=x+y
            else:
                cur_health+=x
            if cur_health>health:
                cur_health=health
                
        if cur_health<1:
            break
    
    return -1 if cur_health<1 else cur_health
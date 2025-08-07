def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        hour = schedules[i]//100
        minutes = schedules[i]%100+10
        if minutes >= 60:
            minutes%=60
            hour+=1
        schedules[i]=hour*100+minutes
    
    week=[1,2,3,4,5,6,7]
    week=week[startday-1:]+week[:startday-1]
    for i in range(len(schedules)):
        for d in range(7):
            if week[d] not in (6, 7) and schedules[i]<timelogs[i][d]:
                break
        else:
            answer+=1
    return answer
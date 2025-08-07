def solution(today, terms, privacies):
    answer = []
    terms = {k: int(v) for k, v in (term.split() for term in terms)}
    today = today.replace('.', '')
    for i, privacy in enumerate(privacies):
        start_date, condition = privacy.split()
        year, month, day = map(int,start_date.split('.'))
        
        month+=terms[condition]
        if month%12 == 0:
            year+=month//12-1
            month=12
        else:
            year+=(month//12)
            month%=12
        day-=1
        
        if day==0:
            month-=1
            day=28
        
        if day<10:
            day="0"+str(day)
        if month<10:
            month="0"+str(month)
        
        end_date=str(year)+str(month)+str(day)
        if today>end_date:
            answer.append(i+1)
        
    return answer
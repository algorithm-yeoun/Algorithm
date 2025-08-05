def solution(n, lost, reserve):
    answer = 0
    duplicates = set(lost) & set(reserve)

    lost = sorted([i for i in lost if i not in duplicates])
    reserve = sorted([i for i in reserve if i not in duplicates])
    
    student=[0 if i in lost else 1 for i in range(n+1)]
    for i in reserve:
        student[i]=2
    
    for i in reserve:
        if i-1>0 and student[i-1] == 0 and student[i]==2:
            student[i-1]=1
            student[i]-=1
        if i+1<n+1 and student[i+1] == 0 and student[i]==2:
            student[i+1]=1
            student[i]-=1
        
    return n-student[1:].count(0)
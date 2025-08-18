def solution(topping):
    answer=0
    topping_older={}
    topping_young={}
    for x in topping:
        topping_older[x] = topping_older.get(x, 0) + 1
    
    for i in topping:
        topping_older[i]-=1
        if topping_older[i] == 0:
            topping_older.pop(i)
        topping_young[i] = topping_young.get(i, 0) + 1
        
        if len(topping_older) == len(topping_young):
            answer+=1
            
    return answer
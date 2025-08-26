from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossing=deque([0]*bridge_length, maxlen=bridge_length)
    truck=truck_weights[::-1]
    cur_weight=0
    
    while not (cur_weight==0 and not truck):
        if cur_weight>0 and not truck:
            cur_weight-=crossing[0]
            crossing.append(0)
        elif truck:
            cur_weight-=crossing.popleft()
            if cur_weight+truck[-1]<=weight:
                cur_weight+=truck[-1]
                crossing.append(truck.pop())
            else:
                crossing.append(0)
        
        cur_weight=0 if cur_weight<=0 else cur_weight
        answer+=1
        
    return answer
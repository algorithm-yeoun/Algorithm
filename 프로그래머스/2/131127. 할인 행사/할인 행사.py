def solution(want, number, discount):
    answer = 0
    total = sorted([item for item, cnt in zip(want, number) for _ in range(cnt)])
    
    for i in range(len(discount)-len(total)+1):
        discount_slice = sorted(discount[i:i+len(total)])
        if total == discount_slice:
            answer+=1
            
    return answer
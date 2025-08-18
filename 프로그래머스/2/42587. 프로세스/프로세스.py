def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    order = []
    
    while priorities:
        max_priorities=max(priorities)
        num = priorities.pop(0)
        loc_num = loc.pop(0)
        if max_priorities == num:
            order.append(loc_num)
        else:
            priorities.append(num)
            loc.append(loc_num)
                
    return order.index(location)+1
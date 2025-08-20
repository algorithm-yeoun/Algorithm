def solution(dirs):
    answer = 0
    recent=(0,0)
    visited=[]
    dirs_dict={'U':(-1,0), 'D':(1,0), 'R':(0,1), 'L':(0,-1)}
    
    for d in dirs:
        x = recent[0]+dirs_dict[d][0]
        y = recent[1]+dirs_dict[d][1]
        if -5<=x<=5 and -5<=y<=5:
            if recent+(x,y) not in visited and (x,y)+recent not in visited:
                visited.append(recent+(x,y))
                visited.append((x,y)+recent)
                answer+=1
            recent=(x,y)
    
    return answer
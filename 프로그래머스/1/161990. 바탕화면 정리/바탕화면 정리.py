def solution(wallpaper):
    answer = [0,0,0,0]
    paper = []
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                paper.append([row, col])
    
    answer[0], answer[2] = min(x := [p[0] for p in paper]), max(x)+1
    answer[1], answer[3] = min(x := [p[1] for p in paper]), max(x)+1
    
    return answer
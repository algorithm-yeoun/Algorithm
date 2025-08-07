def solution(park, routes):
    h=len(park)
    w=len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                answer = [i, j]
                break
    
    dx = {'E': 0, 'W': 0, 'S': 1, 'N': -1}
    dy = {'E': 1, 'W': -1, 'S': 0, 'N': 0}

    for route in routes:
        direction, move = route.split()
        move = int(move)
        nx, ny = answer[0], answer[1]
        blocked = False

        for step in range(1, move + 1):
            x = nx + dx[direction] * step
            y = ny + dy[direction] * step

            if not (0 <= x < h and 0 <= y < w):
                blocked = True
                break

            if park[x][y] == 'X':
                blocked = True
                break

        if not blocked:
            answer = [nx + dx[direction] * move, ny + dy[direction] * move]

    return answer
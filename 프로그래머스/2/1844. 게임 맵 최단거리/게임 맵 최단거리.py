def solution(maps):
    answer = 0
    rows, cols = len(maps), len(maps[0])
    start = (0, 0)
    goal = (rows-1, cols-1)

    visited = [[False]*cols for _ in range(rows)]
    distance = [[-1]*cols for _ in range(rows)]

    # BFS
    queue = [start]
    visited[start[0]][start[1]] = True
    distance[start[0]][start[1]] = 1

    # 상하좌우
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c = queue[0][0], queue[0][1]
        queue.pop(0)
        if (r, c) == goal:
            break
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and maps[nr][nc] == 1:
                    visited[nr][nc] = True
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))
    
    return distance[-1][-1]
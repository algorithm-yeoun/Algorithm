import sys
from collections import deque

# 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(xy):
    queue = deque([xy])
    table[xy[0]][xy[1]] = 2

    while queue:
        xy = queue.popleft()

        for i in range(4):
            xi = xy[0] + dx[i]
            yi = xy[1] + dy[i]

            if 0 <= xi < m and 0 <= yi < n:
                if table[xi][yi] == 1:
                    queue.append([xi, yi])
                    table[xi][yi] = 2


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    table = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        table[x][y] = 1

    for xi in range(m):
        for yi in range(n):
            if table[xi][yi] == 1:
                dfs([xi, yi])
                cnt += 1
    print(cnt)

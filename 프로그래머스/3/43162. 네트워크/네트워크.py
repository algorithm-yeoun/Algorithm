def dfs(start, n, computers, visited):
    stack = [start]

    while stack:
        current = stack.pop()
        visited[current] = True

        for i in range(n):
            if not visited[i] and computers[current][i]:
                stack.append(i)

def solution(n, computers):
    visited = [False] * n
    cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, n, computers, visited)
            cnt += 1

    return cnt
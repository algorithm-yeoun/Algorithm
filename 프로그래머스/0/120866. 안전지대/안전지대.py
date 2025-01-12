def change_zero(board, bomb, n):
    dt = [-1, 0, 1]
    for x in dt:
        for y in dt:
            dx, dy = bomb[0] + x, bomb[1] + y
            if 0 <= dx < n and 0 <= dy < n:
                board[dx][dy] = 1

def get_count_zero(board):
    return sum(row.count(0) for row in board)

def solution(board):
    n = len(board)
    bombs = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
    
    for bomb in bombs:
        change_zero(board, bomb, n)
    
    return get_count_zero(board)
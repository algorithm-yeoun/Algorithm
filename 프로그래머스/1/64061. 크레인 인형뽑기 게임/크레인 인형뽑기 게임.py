def solution(board, moves):
    n=len(board)
    answer = 0
    moves=[i-1 for i in moves]
    stack=[]
    for i in moves:
        for j in range(n):
            if board[j][i]:
                if stack and stack[-1] == board[j][i]:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(board[j][i])
                board[j][i]=0
                break
    return answer
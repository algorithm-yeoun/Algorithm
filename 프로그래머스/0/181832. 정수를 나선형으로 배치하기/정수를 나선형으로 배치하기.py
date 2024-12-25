def solution(n):
    answer = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    
    while top <= bottom and left <= right:
        # 오른쪽으로 이동
        for i in range(left, right + 1):
            answer[top][i] = num
            num += 1
        top += 1
        
        # 아래로 이동
        for i in range(top, bottom + 1):
            answer[i][right] = num
            num += 1
        right -= 1
        
        # 왼쪽으로 이동
        if top <= bottom:
            for i in range(right, left - 1, -1):
                answer[bottom][i] = num
                num += 1
            bottom -= 1
        
        # 위로 이동
        if left <= right:
            for i in range(bottom, top - 1, -1):
                answer[i][left] = num
                num += 1
            left += 1
    
    return answer

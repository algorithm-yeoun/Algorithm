def solution(mats, park):
    answer = -1
    row=len(park)
    col=len(park[0])
    mats=sorted(mats, reverse=True)
    
    def available(row, col, mat):
        for i in range(row, row+mat):
            for j in range(col, col+mat):
                if park[i][j]!='-1':
                    return False
        return True
    
    for m in mats:
        for r in range(row-m+1):
            for c in range(col-m+1):
                if available(r, c, m):
                    return m
                
    return answer
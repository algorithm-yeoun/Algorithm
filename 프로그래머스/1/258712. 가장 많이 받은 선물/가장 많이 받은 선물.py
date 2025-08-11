def solution(friends, gifts):
    answer = {friend: 0 for friend in friends}
    score = {friend: 0 for friend in range(len(friends))}
    matrix = [[0]*len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        g_from, g_to = gift.split()
        matrix[friends.index(g_from)][friends.index(g_to)]+=1
    
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        col_sum = sum(row[i] for row in matrix)
        score[i] = row_sum-col_sum
        
        
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if i != j:
                if matrix[i][j]>matrix[j][i]:
                    answer[friends[i]]+=1
                elif matrix[i][j]<matrix[j][i]:
                    answer[friends[j]]+=1
                else:
                    if score[i]>score[j]:
                        answer[friends[i]]+=1
                    elif score[i]<score[j]:
                        answer[friends[j]]+=1
    
    max_score=max(answer.values())
    
    return max_score
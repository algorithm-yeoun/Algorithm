def solution(numbers, hand):
    answer = ''
    cur_left, cur_right=(0,0), (0,0)
    matrix_left=[["*",7,4,1], [0,8,5,2]]
    matrix_right=[["#",9,6,3], [0,8,5,2]]
    
    def find_index_2d(matrix, target):
        for i, row in enumerate(matrix):
            if target in row:
                return (i, row.index(target))
        return None
    
    for n in numbers:
        if n in matrix_left[0]:
            answer+='L'
            cur_left=find_index_2d(matrix_left,n)
        elif n in matrix_right[0]:
            answer+='R'
            cur_right=find_index_2d(matrix_right,n)
        else:
            mid=find_index_2d(matrix_left,n)
            dis_left=abs(cur_left[0]-mid[0])+abs(cur_left[1]-mid[1])
            dis_right=abs(cur_right[0]-mid[0])+abs(cur_right[1]-mid[1])
            if dis_left < dis_right:
                answer+='L'
                cur_left=mid
            elif dis_left > dis_right:
                answer+='R'
                cur_right=mid
            else:
                if hand=='left':
                    answer+='L'
                    cur_left=mid
                else:
                    answer+='R'
                    cur_right=mid
    
    return answer
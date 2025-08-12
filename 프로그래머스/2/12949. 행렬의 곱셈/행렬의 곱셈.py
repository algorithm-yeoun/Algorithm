def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp=0
            for d in range(len(arr1[0])):
                element= arr1[i][d]*arr2[d][j]
                temp+=element
            answer[i][j]=temp
            
    return answer
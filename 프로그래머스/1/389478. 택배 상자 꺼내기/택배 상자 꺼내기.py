def solution(n, w, num):
    answer = 0
    num_index=-1
    box=[i for i in range(1,n+1)]
    matrix = [box[i:i+w] for i in range(0, len(box), w)]   
    
    for line in range(1,len(matrix),2):
        matrix[line]=matrix[line][::-1]
        if len(matrix[line])<w:
            matrix[line]=[0 for _ in range(w-len(matrix[line]))]+matrix[line]
    
    if len(matrix[-1])<w:
        matrix[-1]+=[0 for _ in range(w-len(matrix[-1]))]
        
    for line in matrix:
        if num in line:
            num_index = line.index(num)
        if num_index>-1 and line[num_index]:
            answer+=1
    
    return answer
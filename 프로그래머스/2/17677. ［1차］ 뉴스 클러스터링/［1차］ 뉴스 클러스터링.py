def solution(str1, str2):
    answer = 0
    A = []
    B = []
    
    for i in range(len(str1)-1):
        temp = str1[i]+str1[i+1]
        if temp.isalpha():
            A.append(temp.upper())
    
    for i in range(len(str2)-1):
        temp = str2[i]+str2[i+1]
        if temp.isalpha():
            B.append(temp.upper())
    
    if not A and not B:
        return 65536
    
    # 교집합
    intersection = []
    for i in A:
        if i in B:
            intersection.append(i)
            B.remove(i)
    
    union = A + B   # 합집합
    
    sub_result = len(intersection) / len(union)
    return int(sub_result*65536)
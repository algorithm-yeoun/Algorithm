def solution(s):
    answer = 0
    start, left, right = 0, 0, 0
    
    for i in range(0, len(s)):
        if s[start]==s[i] or start==i:
            left+=1
        else:
            right+=1
        if left==right:
            answer+=1
            left, right = 0, 0
            start=i+1 
    
    return answer if left == right else answer+1
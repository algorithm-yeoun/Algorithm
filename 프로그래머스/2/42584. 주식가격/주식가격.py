def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack=[0]
    n=len(prices)
    
    for i in range(1, n):
        while stack and prices[stack[-1]]>prices[i]:
            l=stack.pop()
            answer[l]=i-l
        stack.append(i)
    
    for i in stack:
        answer[i]=n-i-1
         
    return answer
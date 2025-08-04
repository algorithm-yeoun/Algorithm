def solution(dartResult):
    answer = 0
    stack=[]
    start=0
    
    def S(n):
        return n**1
    
    def D(n):
        return n**2
    
    def T(n):
        return n**3
    
    for i in range(1,len(dartResult)):
        if dartResult[i].isalpha():
            score=dartResult[start:i+1]
            teritory=score[-1]
            if teritory == 'S': 
                score=S(int(score[:-1]))
            elif teritory == 'D':
                score=D(int(score[:-1]))
            elif teritory == 'T':
                score=T(int(score[:-1]))
            stack.append(score)
            start=i+1
        elif dartResult[i] == '*':
            stack.append(dartResult[start:i+1])
            start+=1
        elif dartResult[i] == '#':
            stack[-1]*=(-1)
            start+=1
    
    while '*' in stack:
        star=stack.index('*')
        if star==1:
            stack[0]*=2
            stack.pop(star)
        else:
            stack[star-1]*=2
            stack[star-2]*=2
            stack.pop(star)
        
    return sum(stack)
def solution(ingredient):
    answer = 0
    stack=''
    for i in ingredient:
        stack+=str(i)
        if stack[-4:] == '1231':
            answer+=1
            stack=stack[:-4]
    return answer
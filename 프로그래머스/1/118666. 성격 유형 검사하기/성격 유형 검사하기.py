def solution(survey, choices):
    answer = ''
    pairs = ["RT", "CF", "JM", "AN"]
    mbti = {"R":0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = {1:-3, 2:-2, 3:-1, 4:0, 5:1, 6:2, 7:3}
    
    for i in range(len(survey)):
        if score[choices[i]]<0:
            mbti[survey[i][0]]+=abs(score[choices[i]])
        elif score[choices[i]]>0:
            mbti[survey[i][1]]+=abs(score[choices[i]])

    for x, y in pairs:
        if mbti[x] > mbti[y]:
            answer += x
        elif mbti[x] < mbti[y]:
            answer += y
        else:
            answer += min(x, y)
    
    return answer
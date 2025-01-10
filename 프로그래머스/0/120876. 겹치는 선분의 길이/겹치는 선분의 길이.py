def solution(lines):
    answer = 0
    line=[set(range(line[0],line[1])) for line in lines]
    
    one=line[0]&line[1]
    two=line[0]&line[2]
    three=line[1]&line[2]
    
    answer=len(one|two|three)
    
    return answer

# 잘못된 방법

# answer+=len(line[0]&line[1])
# answer+=len(line[0]&line[2])
# answer+=len(line[1]&line[2])

# 3번째 테스트 케이스에서 오류 
# {3, 4} {1, 2, 3, 4} {3, 4, 5, 6, 7, 8} 
# {3, 4}를 중복 계산

# 각 선분끼리 교집합을 합집합으로 계산한 뒤 길이를 재야 함
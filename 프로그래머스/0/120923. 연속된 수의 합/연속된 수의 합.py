def solution(num, total):
    start=total//num-(num-1)//2
    answer=[i for i in range(start,start+num)]
    return answer
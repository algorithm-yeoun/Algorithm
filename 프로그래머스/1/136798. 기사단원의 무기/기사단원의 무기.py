def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        count=0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                count += 1
                if i ** 2 != n:
                    count += 1
        
        answer+=(power if count>limit else count)
    return answer
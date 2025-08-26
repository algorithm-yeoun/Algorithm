from itertools import permutations

def solution(numbers):
    answer = 0
    numbers=[i for i in numbers]
    all_combinations = set()
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for r in range(1, len(numbers)+1):
        for p in permutations(numbers, r):
            num = int(''.join(map(str, p)))
            if num not in (0, 1):
                all_combinations.add(num)
    
    com = sorted(all_combinations)
    
    for i in com:
        if is_prime(i):
            answer+=1
    
    return answer
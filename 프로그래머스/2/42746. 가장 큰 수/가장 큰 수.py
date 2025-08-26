def solution(numbers):
    
    sorted_numbers = sorted(numbers ,key=lambda x: str(x)*4, reverse=True)
    
    return ''.join(list(map(str,sorted_numbers))) if sorted_numbers[0]!=0 else '0'
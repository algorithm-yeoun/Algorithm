def change(n, base):
    result=''
    num=n
    while num>0:
        result=str(num%base)+result
        num//=base
    return result

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solution(n, k):
    answer = 0
    
    change_num=change(n, k).split('0')
    
    for num in change_num:
        if num and is_prime(int(num)):
            answer+=1
            
    return answer
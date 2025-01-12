def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    one, two=[numer1,denom1], [numer2, denom2]
    denom_lcm=lcm(denom1, denom2)
    
    # 분수 덧셈
    one=[i*(denom_lcm//denom1) for i in one]
    two=[i*(denom_lcm//denom2) for i in two]
    answer=[one[0]+two[0],denom_lcm]
    
    # 기약 분수
    nd_gcd=gcd(answer[0],answer[1])
    answer=[i//nd_gcd for i in answer]
    
    return answer
# 피보나치 수열
def solution(n):
    if n==1:
        answer=1
    else:
        array=[0]*n
        array[0]=1
        array[1]=2

        for i in range(2,n):
            array[i]=array[i-1]+array[i-2]

        answer=array[n-1]%1234567

    return answer
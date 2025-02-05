def comb(arr, n):
    result=[]
    if n>len(arr):
        return result
    
    if n==1:
        for i in arr:
            result.append([i])
    elif n>1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]]+j)
                
    return result

def solution(nums):
    answer = 0
    ch = [0]*3000
    for i in range(2, 3000):
        for j in range(i*2, 3000, i):
            ch[j]=1
    
    for i in comb(nums,3):
        if ch[sum(i)]==0:
            answer+=1

    return answer
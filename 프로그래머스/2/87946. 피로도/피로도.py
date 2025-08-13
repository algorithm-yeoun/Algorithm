def solution(k, dungeons):
    answer = 0
    
    def permute(nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                permute(nums, path, used, result)
                path.pop()
                used[i] = False

    nums = [i for i in range(len(dungeons))]
    result = []
    used = [False] * len(nums)
    permute(nums, [], used, result)

    for p in result:
        k2=k
        cnt=0
        for i in p:
            if k2>=dungeons[i][0]:
                k2-=dungeons[i][1]
                cnt+=1
            else:
                break
        answer=max(answer,cnt)
        
    return answer
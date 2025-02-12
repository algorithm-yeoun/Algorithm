def solution(n, m, section):
    color=[0]*(n+1)
    answer = 0
    for i in section:
        if color[i]==0:
            answer+=1
            for j in range(i,i+m):
                if j<=n:
                    color[j]=1
    return answer
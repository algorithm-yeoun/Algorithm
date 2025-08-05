def solution(X, Y):
    count_x = {str(i): 0 for i in range(10)}
    count_y = {str(i): 0 for i in range(10)}

    for i in X:
        count_x[i] += 1
    for i in Y:
        count_y[i] += 1

    answer = ''
    for i in range(9, -1, -1):
        s = str(i)
        count_d = min(count_x[s], count_y[s])
        answer += s * count_d

    if not answer:
        return "-1"
    elif answer[0] == '0':
        return "0"
    return answer
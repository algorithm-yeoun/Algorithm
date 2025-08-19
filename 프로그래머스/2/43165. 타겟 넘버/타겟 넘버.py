def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]

    while stack:
        index, current = stack.pop()

        if index == len(numbers):
            if current == target:
                answer += 1
            continue

        num = numbers[index]

        stack.append((index + 1, current + num))
        stack.append((index + 1, current - num))
        
    return answer
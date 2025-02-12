def solution(my_string):
    num_str=''
    for i in my_string:
        if i.isalpha():
            num_str+=' '
        else:
            num_str+=i

    return sum(int(i) for i in num_str.split())
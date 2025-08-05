def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alphabet=alphabet.replace(i,'')
    length=len(alphabet)
    for i in s:
        result=alphabet.index(i)+index
        answer+=alphabet[result%length]
    return answer
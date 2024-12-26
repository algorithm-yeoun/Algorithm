def solution(babbling):
    answer = 0
    arr = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for a in arr:
            word = word.replace(a,'1')
        
        word = ''.join([c for c in word if not c.isdigit()])
        
        if not word:
            answer+=1
    
    return answer

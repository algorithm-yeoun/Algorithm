def solution(word):
    answer = []
    gather = 'AEIOU'
    
    def recursion(letter, max_len=5):
        if 1 <= len(letter) <= max_len:
            answer.append(letter)
        if len(letter) == max_len:
            return
        
        for l in gather:
            recursion(letter+l, max_len)
            
    recursion('')
    
    return answer.index(word)+1
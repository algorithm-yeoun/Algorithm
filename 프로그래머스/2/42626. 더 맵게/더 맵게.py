import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K and len(scoville)>=2:
        heapq.heappush(scoville, heapq.heappop(scoville)+(heapq.heappop(scoville)*2))
        answer+=1
    
    
    return answer if scoville[0]>=K else -1
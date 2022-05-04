import heapq

def solution(scoville, K):
    answer = 0
    
    # scoville.sort()
    heapq.heapify(scoville)
    
    i = 0
    while scoville[0] < K:
        if(len(scoville) == 1):
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        i = i + 1
        answer = i
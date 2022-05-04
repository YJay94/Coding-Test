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



--------------------------------
int()
bin()
oct()
hex()
--------------------------------

list(str) <= 문자열1글자식 자르기


# re모듈
re.match("one", string)
findall()
match()
split()



string.find('a')
string.index('a')
# 딕셔너리 배열 정렬방법

dic_value = {"파이썬": 4, "코딩":2, "프로그래밍":1, "Python":1}

sorted(dic_value.items(), key = lamda x:x[1])
print(sorted_desc_dict)


heap과 deque에 대한 바른 이해

datetime.date(2022.05.09)
datetime.date.today()
datetime.timedelta(days=50)

calendar.isleap()





from itertools import combinations
from collections import deque
import pprint
import heapq


def solution(people, limit):
    answer = 0
    
    p = sorted(people)
    d = deque(p)
    
    while d:
        if(len(d) == 1):
            answer += 1
            break
        elif(d[0] + d[-1] <= limit):
            answer += 1
            d.pop()
            d.popleft()
        else:
            answer += 1
            d.pop()
        
    return answer


if문 돌리는거말고 while제대로 활용하기


range(1,100)
 1부터 99까지

range(100)
 0부터 99까지



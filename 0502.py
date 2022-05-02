# 파이썬 중복확인
count={}
lists = ["a","a","b",'apple','w','wf']
for i in lists:
    try: count[i] += 1
    except: count[i]=1
print(count)


from collections import Collection
from typing import Counter

word = ['a','b','a','a','c']
Counter(word)

결과값 : {'a': 2, 'b': 1, 'apple': 1, 'w': 1, 'wf': 1}

--------------------------------------------------

from collections import Counter

def solution(participant, completion):    
    answer = Counter(participant)-Counter(completion)
    print(list(answer.keys())[0])
    
    # answer = 
    # return answer




배열쓰고 그냥 print(array)가 아나ㅣ라 print(list(array)) 이렇게 써야함


enumerate


딕셔너리공부해라 제발....
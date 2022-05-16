from functools import reduce


result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# ((((1+2)+3)+4)+5)
print(result)

# 15


                                    14
arr1 : [[1, 2, 3], [4, 5, 6]]       25
                                    36
arr2 : [[1, 4], [2, 5], [3, 6]]

return : [[14, 32], [32, 77]]



def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sum = 0
        for j in range(i,n+1):
            sum += j
            if(sum == n):
                print(sum, i, j)
                answer += 1
            if(sum >= n):
                break
    
    return answer




for x in range(4):
  if x == 2:
    print ('loop out')
    break
else:
  print ('loop end')



위 예제의 경우는 x =2 에서 루프를 빠져나오기때문에, else문이 실행이 되지 않고
'loop out' 이 출력이 되고,



for x in range(4):
  # nop
  pass
else:
  print ('loop end')


위와 같은 경우는 , for loop가 break없이 빠져나왔으므로 'loop end' 가 출력이 된다.



from functools import reduce


result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
# ((((1+2)+3)+4)+5)
print(result)

# 15


>>> import math
>>> math.gcd(60, 100, 80)
20


>>> import math
>>> math.lcm(15, 25)
75


TypeError: Object of type int64 is not JSON serializable
-> 각 항목별 int()넣기




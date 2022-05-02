from collections import Counter

def solution(N, stages):
    answer = []
    
    fit_stages = Counter(stages)
    
    # print(fit_stages)
    # print(fit_stages[2])
    
    key_fit_stages = fit_stages.keys()
    # print(key_fit_stages)
    
    value_fit_stages = fit_stages.values()
    # print(value_fit_stages)
    
    zip_arr = sorted(list(zip(key_fit_stages, value_fit_stages)))
    print(zip_arr)
    
    t = 0
    count = 0
    arr_rate = []
    for i in zip_arr:
        sum_arr = zip_arr[t:]
        # count = count + sum_arr[t][1]
        # print(sum_arr)
        num = 0
        for j in sum_arr:
            num = num + j[1]
        
        # print(sum_arr[0][1])
        # print(num)
        # print(sum_arr[0][0])
        
        if(sum_arr[0][0] == N+1):
            arr_rate.append(0)
        elif((sum_arr[0][1] / num) != 0):
            arr_rate.append(sum_arr[0][1] / num)
        
        t = t + 1
    
    print(sorted(list(zip(arr_rate, sorted(key_fit_stages))),reverse = True))
    
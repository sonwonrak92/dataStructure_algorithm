'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/04

두 번째 과제 -01
:: 정렬된 리스트에 원소 삽입::

'''

# Test Case
L = [20, 37, 58, 72, 91]

def solution(L, x):
    answer = L
    last = len(L) - 1
    first = 0
    #들어온 x의 값이 리스트에서 가장 큰 값일 경우 마지막에 append한다.
    if L[last] < x :
        answer.append(x)
        return answer
    #들어온 x의 값이 리스트에서 가장 작은 값일 경우 제일 앞에 insert한다.
    elif L[first] > x :
        answer.insert(0, x)
        return answer 
    else :
        for value in L : #리스트를 반복하면서 비교 후 작은 경우 인설트        
            if value >= x : 
                changeIdx = answer.index(value)
                answer.insert(changeIdx, x)                      
                return answer
                
    return answer

print(solution(L, 58) )
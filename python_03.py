'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/06

세 번째 과제
::이진탐색 구현하기::

최초의 값이 중간 값과 같으면 중간 값의 인덱스를 리턴한다
최초의 값이 중간인덱스 값 보다 작으면 처음값과 중간값의 사이값과 비교한다
여기서 중간인덱스를 다시 마지막 인덱스로 설정한다
최초의 값이 중간 값 보다 크면 중간값과 마지막값의 사이값과 비교한다 여기서 중간값은 다시 처음 인덱스가 된다
따라서 최초의 인덱스, 중간 인덱스 , 마지막 인덱스, 결과인덱스 변수가 필요하다

'''
# Test Case
test01 = [1,2,3,4,5]
test02 = [55]
test03 = [1,2,3,4,5,6,7,8,22,44,66,321]

def solution(L, x):
    if x in L :        
        stdIdx = 0
        endIdx = len(L) - 1 
        
        while stdIdx <= endIdx :
            middleIdx = (stdIdx + endIdx) // 2            
            print('start : {}'.format(stdIdx))
            print('middle : {}'.format(middleIdx))
            print('endIdx : {}'.format(endIdx))
            print(L[middleIdx])
            print(x)
            if L[middleIdx] == x :
                return middleIdx
            elif L[middleIdx] > x :                 
                endIdx = middleIdx - 1
                print('end : {}'.format(endIdx))
            elif L[middleIdx] < x :
                stdIdx = middleIdx + 1   
                print('std : {}'.format(stdIdx))
                    
    else :
        answer = -1

    return answer

test =    [2, 3, 5, 6, 9, 11, 15]
print(solution(test03,2))
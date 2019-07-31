'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/07/31

첫 번째 과제
::리스트 첫 번째 값과 마지막 값의 합::

'''
# Test Case
test01 = [1,2,3,4,5]
test02 = [55]
test03 = [22,44,66,321,23]

def solution(testList):
    '''
    접근 방법.
    - 리스트 타입의 자료구조에서 데이터를 가져오는 방법에 대해서 고민해본다.
    
    풀이.
    1.리스트에서 값을 가져오기 위해서는 인덱스를 이용하는 방법이 있다.
    2.따라서 첫 번째 인덱스와 마지막 인덱스를 구하면 쉽게 풀 수 있다.
    3.대부분의 자료구조에서 첫 번째 값이 있는 곳은 0번 인덱스다. 따라서 첫 번째 인덱스를 0으로 설정한다.
    4.마지막 인덱스의 경우 리스트의 길이를 구한 후 -1을 하면 마지막 인덱스를 구할 수 있다.
    '''

    #첫 번째 인덱스
    getFirstIdx = 0
    #마지막 인덱스
    getLastIdx = len(testList) - 1 
    
    firstValue = testList[getFirstIdx]
    lastValue = testList[getLastIdx]

    print(firstValue + lastValue)

# output : 6
solution(test01)   

# output : 110
solution(test02)  

# output : 45
solution(test03)  
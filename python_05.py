'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/06

다섯 번째 과제
::재귀함수를 이용하여, 이진탐색 구현하기::


'''
# Test Case
test01 = [1,2,3,4,5]
test02 = [55]
test03 = [1,2,3,4,5,6,7,8,22,44,66,321]

def solution(L, x, l, u):
    if L.count(x) > 0 :
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return solution(L,x,L[mid]+1,u)
    elif x < L[mid]:
        return solution(L,x,l,L[mid]-1)

    else:
        return -1



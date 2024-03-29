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
    if L.count(x) == 0 :
        return -1
    mid = (l + u) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]: # x의 값이 중간값보다 작을 경우 탐색최대치를 중간값보다 -1한다
        return solution(L,x,l,L[mid]-1)
    else :  # x의 값이 중간값보다 큰 경우 탐색최저치를 중간값보다 +1한다
        return solution(L,x,L[mid]+1,u)

print(solution(test03, 4, 0, 11))



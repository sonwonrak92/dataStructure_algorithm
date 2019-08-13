'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 두 번째 과제
::연결 리스트 순회::

'''
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

# 과제를 위한 메서드 작성부분
def traverse(self):
    result = [] #최초의 값은 빈 값이다.
    curr = self.head #현재 노드를 헤드로 지정한다.
    while curr is not None: # 만약 헤드가 비어있지 않다면 현재 노드의 데이터를 어팬드한 후 넥스트를 현재 노드로 지정한다.
        result.append(curr.data)
        curr = curr.next
    return result

# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
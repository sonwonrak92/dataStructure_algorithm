'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 다섯 번째 과제 중 01
::양방향 연결 리스트 역방향 순회::

'''
class Node:
    
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

#과제로 구현해야되는 부분
    def reverse(self):
        '''
        1.거꾸로 진행해봅시다. 양방향이니까
        2.거꾸로니까 끝을 의미하는 테일을 잡고 테일의 prev를 타고가면 될 것 같습니다.
        3.우선 테일의 이전 노드가 있는지 부터 확인하겠습니다.
        4.테일의 이전 노드가 있으면, 이전 노드로 이동 후 데이터를 추출하고 다시 이전 노드의 이전 노드가 있는지 확인 한 후 이동 < - while조건으로 쓰면될듯.
        '''

        result = []
        curr = self.tail #현재 노드를 테일로 지정한다
        while curr.prev.prev: # 현재노드의 prev는 이전 노드를 의미하면 이전 노드의 prev는 그것의 이전 노드를 의미한다.
            curr = curr.prev # 이전 노드로 이동.
            result.append(curr.data) # 이전 노드의 데이터를 결과 리스트에 append한다.
            #이전 노드의 prev에 노드가 있으면 다시 이전노드로 이동해서 같은 걸 반복해야한다. <- while조건 도출
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


def solution(x):
    return 0
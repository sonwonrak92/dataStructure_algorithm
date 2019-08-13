'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 다섯 번째 과제 중 03
:: 양방향 연결 리스트 노드 삭제::

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


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
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

#과제구현부분
    def popAfter(self, prev):
        '''
        1.일단 이전노드가 파라미터로 들어오기때문에
        2.이전 노드의 넥스트를 알 수 있고 이것을 지우면서 해야되는 절차를 구현하면 된다.
        3.지워질 넥스트 노드의 next를 이전 노드의 next로 할당하고
        4.넥스트 노드의 next에 해당하는 노드의 prev에 이전 노드를 할당하면 끝.
        5.주의할점은 파라미터로 들어오는 prev가 tail이면 after 노드가 none이기에 그냥 리턴처리해야됨.
        '''
        curr = prev.next #이전 노드의 next가 지워질 노드
        next = curr.next # 지워질 노드의 next를 next에 할당
        prev.next=next #이전 노드의 next에 지워질 노드의 next를 할당
        next.prev = prev #지워질 노드의 next에 해당하는 노드의 prev에 이전 노드를 할당
        self.nodeCount-=1
        return curr.data
#과제구현부분
    def popBefore(self, next):
        '''
        비슷함
        '''
        curr = next.prev
        prev = curr.prev
        prev.next=next
        next.prev = prev
        self.nodeCount-=1
        return curr.data
#과제구현부분
    def popAt(self, pos):
        if pos<0 or pos> self.nodeCount:
            raise IndexError
        else:
            curr = self.getAt(pos)
            prev = curr.prev
            next = curr.next
            prev.next=next
            next.prev = prev
            self.nodeCount-=1
            return curr.data


def solution(x):
    return 0
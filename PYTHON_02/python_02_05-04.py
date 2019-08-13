'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 다섯 번째 과제 중 04
:: 양방향 연결 리스트의 병합::

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

#과제 구현 부분
    def concat(self, L):
        '''
        1. 둘다 노드카운트가 0이면 none
        2. L만 노드카운트가 0이면 그대로 리턴
        3. 자기자신의 노드카운트가 0이면 L을 그대로 흡수 -> self = L 하려고했는데 테스트케이스에서 터짐
        4. 나머지 경우에는 자기자신의 테일의 넥스트

        '''

        if self.nodeCount == 0 and L.nodeCount == 0:
            return None

        elif L.nodeCount == 0:
            pass

        elif self.nodeCount == 0 :
            self.head.next = L.head.next
            self.tail.prev = L.tail.prev
            self.nodeCount += L.nodeCount

        else:
            self.tail.prev.next = L.head.next #테일은 현재 더미테일이기에 더미테일의 이전 노드의 넥스트 값을 더미테일로 두지말고 L의 헤드더미 넥스트 값을 이어주면됨.
            L.head.next.prev = self.tail.prev
            self.tail.prev = L.tail.prev
            L.tail.prev.next = self.tail

        return self


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


def solution(x):
    return 0
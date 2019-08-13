'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 다섯 번째 과제 중 02
:: 양방향 연결 리스트 노드 삽입::

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

#과제 구현부분
    def insertBefore(self, next, newNode):
        '''
        1.일단 넥스트 노드가 파라미터로 들어오기 때문에
        2.넥스트 노드의 prev를 가져올 수 있고
        3.넥스트 노드와 이전 노드사이에 뉴노드를 넣어야되기때문에
        3-2. 일단 뉴노드의 next, prev에 각각 넥스트 노드를 넣고 이전 노드를 넣어준다.
        4.이전 노드의 넥스트에 뉴노드를 넣고
        5.넥스트 노드의 prev에 뉴노드를 넣으면 게임 끝
        '''
        prev = next.prev #일단 이전 노드를 가져오고
        newNode.next = next # 뉴노드의 next에 넥스트 노드를 넣고
        newNode.prev = prev # 뉴노드의 prev에는 이전 노드를 넣는다.
        '''
        먼저 뉴노드의 next와 prev를 세팅하는게 중요함. 이거 때문에 시간 잡아먹었습니다. ㅜ
        '''
        prev.next = newNode #그리고 이전 노드의 next에 뉴노드를 넣고
        next.prev = newNode # 넥스트 노드의 prev에 뉴노드를 넣고
        self.nodeCount += 1 #카운트 +1하면 끝
        return True


def solution(x):
    return 0

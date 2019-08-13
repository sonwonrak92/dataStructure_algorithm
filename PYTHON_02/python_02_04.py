'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 네 번째 과제
::dummy head 를 가지는 연결 리스트 노드 삭제::

'''
class Node:
    
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        '''
        1. 파라미터로 넘어오는 prev는 지울 노드의 이전 노드를 의미한다.
        2. 그렇기에 이전 노드의 넥스트가 현재 지울 노드가 된다.
        3. 만약 파라미터로 넘어온 이전 노드의 넥스트가 없으면 이건 태일아!!. 아구몬        

        '''
        if prev.next is None or prev == self.tail : #이전 노드의 넥스트값이 none이면 이전 노드가 테일이다. 즉 테일 다음 노드는 존재하지 않기에 리턴해줘야한다.
            return None
        
        curr = prev.next #curr.next == prev.next.next 같은 의미^^

        if curr.next is None: #지울 노드가 테일일 경우 이전 노드에게 테일의 역할을 부여해야한다. 즉 이전 노드의 넥스트를 none으로 줘야됨.
            self.tail=prev
            prev.next = None

        else:
            prev.next = curr.next #이전 노드의 넥스트값에에 지울 노드의 넥스트값을 줘야함.

        self.nodeCount -=1
        return curr.data

#과제로 구현해야되는 부분
    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError

        else:
            prev=self.getAt(pos-1) #이전 노드 가져오기
            return self.popAfter(prev) #popAfter이용해서 지워버리기!


def solution(x):
    return 0
'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/13

챕터2 - 세 번째 과제
::연결리스트 노드 삭제::

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


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

#과제 작성 부분
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount: #포지션 값이 1보다 작거나 노드의 길이보다 큰 경우에는 꺼낼 수 없다.
            raise IndexError

        elif self.nodeCount == 1 and pos == 1: #노드가 1개 들어있으며 포지션을 1로 줄 경우 헤드를 의미한다. 따라서 헤드데이터를 삭제하란 말임.
            data = self.head.data
            self.head = None
            self.tail = None

        else: #이외의 모든 조건에 대해서 노드를 삭제한다.
            prev = self.getAt(pos-1) #먼저 getAt을 이용해서 넘어온 포지션 값의 이전 노드를 찾고 prev라는 변수에 넣는다.
            data = prev.next.data #이전 노드의 넥스트 = 현재 지울 노드

            if pos == self.nodeCount: #만약 포지션의 값이 현재 노드카운트와 같으면 테일을 의미한다. 헤드가 아닌 이유는 위에서 걸러지기 때문이다.
                self.tail = prev
                prev.next = None

            else: 
                #포지션이 테일이 아닌 중간 값일 경우 이전 노드의 넥스트 = 현재 노드이며, 현재 노드는 사라지기에 현재 노드의 넥스트를 이전 노드의 넥스트에 줄 필요가 있다.
                #즉 현재 노드의 넥스트값을 이전 노드의 넥스트 값에 준다. 쓰다보니 복잡하네요. 죄송합니다.
                prev.next = prev.next.next 

        self.nodeCount -= 1

        return data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
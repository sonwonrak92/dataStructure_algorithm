'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/27

챕터4 - 네 번째 과제
::이진 트리의 넓이 우선 순회::

'''
class ArrayQueue:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal=[]
        q=ArrayQueue()

        if self.root:
            q.enqueue(self.root)

        while (q.isEmpty()==False):
            node=q.dequeue()
            traversal.append(node.data)
            if node.left:
                q.enqueue(node.left)

            if node.right:
                q.enqueue(node.right)

        return traversal


def solution(x):
    return 0
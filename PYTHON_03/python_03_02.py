'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/20

챕터3 - 두 번째 과제
::중위표현 수식 --> 후위표현 수식::

'''
class ArrayStack:
    
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0
   
    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    S = ArrayStack()
    for c in expr:
        if c in '({[':  #괄호가 나올 경우 연산자스택에 넣는다.          
            S.push(c)

        elif c in match:    #닫는 괄호가 나올 경우에는 여는 괄호를 담는 스택이 비어있는지 확인한다.
            if S.isEmpty() : #비어있다면 여는 괄호가 없이 닫는 괄호만 존재한다는 것이므로 리턴한다.
                return False
            else:                
                t = S.pop() 
                if t != match[c]: #닫는 괄호끼리 짝이 안맞는것이 존재하면 리턴한다.
                    return False

    return S.isEmpty()

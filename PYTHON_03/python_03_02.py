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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for token in S :
        if token in prec :#연산자면 스택에 푸쉬한다 
            if not opStack.isEmpty() :  #스택이 비어있지 않으면,              
                if token is '(' : #여는 괄호는 무조건 푸쉬만한다
                    opStack.push(token)

                elif prec[token] <= prec[opStack.peek()] : #스택에 존재하는 연산자의 우선순위가 높거나 같을 경우 스택의 연산자를 팝 한 후 어팬드하고 낮은 연산자를 푸쉬한다
                    answer+= (opStack.pop())
                    opStack.push(token)

                else : #스택에 존재하는 연산자가 우선순위가 낮을 경우 그대로 푸쉬만한다.
                    opStack.push(token)

            else : #스택이 비어있으면 그냥 푸쉬한다
                opStack.push(token)              
        elif token is ')' : #닫는 괄호를 만나면 닫는괄호 이전까지의 스택을 모두 어팬드한다.
            while True:
                if opStack.peek() is '(' : #여는괄호는 어팬드하지않고 뽑기만 하고 브레이크한다
                    opStack.pop()
                    break 
                answer+= (opStack.pop())        

        else : #숫자면 숫자에 어팬드하고
            answer+= (token)

    #남은 스택을 모조리 어팬드친다.
    while not opStack.isEmpty() :
        answer += (opStack.pop())       
    
    return answer
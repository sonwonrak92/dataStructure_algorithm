'''

### Python Algorithm Study ###
# author  : laziness
# date    : 2019/08/20

챕터3 - 세 번째 과제
::후위표현 수식 계산::

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList :
        if token in prec :#연산자면 스택에 푸쉬한다 
            if not opStack.isEmpty() :  #스택이 비어있지 않으면,              
                if token is '(' : #여는 괄호는 무조건 푸쉬만한다
                    opStack.push(token)

                elif prec[token] <= prec[opStack.peek()] : #스택에 존재하는 연산자의 우선순위가 높거나 같을 경우 스택의 연산자를 팝 한 후 어팬드하고 낮은 연산자를 푸쉬한다
                    postfixList.append(opStack.pop())
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
                postfixList.append(opStack.pop())        

        else : #숫자면 숫자에 어팬드하고
            postfixList.append(token)

    #남은 스택을 모조리 어팬드친다.
    while not opStack.isEmpty() :
        postfixList.append(opStack.pop())       
    print(postfixList)
    return postfixList


def postfixEval(tokenList):
#들어오는 수식에 대해서 피연산자를 만나면 푸시한다.
#연산자를 만나면 2개의 피연산자를 팝한후 해당 연산자로 계산을 합니다
#계산된 값을 다시 푸시합니다.
#이것을 반복합니다.
#스택이 비어있으면 리턴한다.

    val = ArrayStack()

    for item in tokenList :

        if type(item) is int :
            val.push(item)            
        
        elif item in '+-*/': #연산자가 등장할 경우 앞의 두 피연산자를 해당 연산자로 연산후 푸쉬한다
            second = val.pop()
            first = val.pop()

            if item is '+' :
                val.push(first+second)            
            elif item is '-' :
                val.push(first-second)            
            elif item is '*' :
                val.push(first*second)            
            elif item is '/' : 
                val.push(first/second)                       
        
        else : #피연산자가 들어올 경 우
            return val.pop()

    return val.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
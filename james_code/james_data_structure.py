import string

from pythonds import Queue, Deque
from pythonds.basic import Stack


# 1-6 最大公约数
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm
    return n


# 3-1 用python实现栈
class JamesStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 3-4 括号匹配
def matches(open, close):
    opens = "([{"
    closers = ")]}"

    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


# 3-6 将十进制数转换成任意进制数
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]

    return newString


# 3-7 从中序表达式到后序表达式的转换
def infixToPostfix(infixexp):
    prec_dict = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opStack = Stack()
    postfixList = []

    tokenList = infixexp.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec_dict[opStack.peek()] >= prec_dict[token]):
                postfixList.append(opStack.pop())

            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


# 3-8 实现后序表达式的计算
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


# 3-9 用python实现队列
class JamesQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.isEmpty() == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# 3-10 传土豆模拟程序(约瑟夫环)
def hotPotato(nameList, num):
    simQueue = Queue()

    for name in nameList:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())
        simQueue.dequeue()

    return simQueue.dequeue()


# 3-14 用python实现双端队列
class JamesDeque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFont(self):
        self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# 3-15 回文检测器
def palchecker(aString):
    charDeque = Deque()

    for ch in aString:
        charDeque.addRear(ch)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


# 3-16 Node类
class JamesNode:
    def __init__(self, initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    def isEmpty(self):
        return self.head == None


# 4-3 将整数转换成以2-16为进制基数的字符串
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString(n % base)


# 4-8 汉诺塔问题
def moveDisk(fp, tp):
    print("moving disk from %d to %d\n" % (fp, tp))


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def main():
    print("james_data_structure start...")

    moveTower(3, 1, 2, 3)


if __name__ == '__main__':
    main()

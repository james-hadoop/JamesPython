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


def main():
    print("james_data_structure start...")


if __name__ == '__main__':
    main()

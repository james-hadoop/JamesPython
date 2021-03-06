"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""

# 链表节点
from twisted.web import static


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 复杂链表节点
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def print_chain(node):
    while node:
        print(node.val)
        node = node.next


class Solution:
    def __init__(self):
        ## 两个栈实现队列
        self.acceptStack = []
        self.outputStack = []

        ## 包含min函数的栈
        self.stask = []
        self.minValue = []

    """
        [00_斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

    # 题目描述
    # 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
    # n <= 39
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci2(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        a = 1
        b = 0

        ret = 0
        for i in range(0, n - 1):
            ret = a + b
            b = a
            a = ret
        return ret

    """
        [01_跳台阶](https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

    # 题目描述
    # 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
    def jump_floor(self, number):
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        ret = 0
        a = 1
        b = 2
        for i in range(3, number + 1):
            ret = a + b
            a = b
            b = ret

        return ret

    """
        [06_二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    def find(self, target, array):
        row_cnt = len(array)
        i = 0
        col_cnt = len(array[0])
        j = len(array[0]) - 1

        while i < row_cnt and j >= 0:
            value = array[i][j]
            if value == target:
                return True
            elif value > target:
                j -= 1
            else:
                i += 1
        return False

    """
        [07_替换空格](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 请实现一个函数，将一个字符串中的每个空格替换成“ % 20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
    def replace_space(self, s):
        strLen = len(s)

        aaa = []
        for i in range(strLen - 1, -1, -1):
            if s[i] == " ":
                aaa.append("0")
                aaa.append("2")
                aaa.append("%")
            else:
                aaa.append(s[i])

        aaa.reverse()
        return ''.join(aaa)

    """
        [08_用两个栈实现队列](https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    def push(self, node):
        self.acceptStack.append(node)

    def pop(self):
        if self.outputStack == []:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())

        if self.outputStack == []:
            return self.outputStack.pop()
        else:
            return None

    """
        [二分查找]
    """

    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1

        while left < right:
            mid = (left + right) >> 1
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    """
        [09_旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    # 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
    # 例如数组
    # {3, 4, 5, 1, 2}
    # 为
    # {1, 2, 3, 4, 5}
    # 的一个旋转，该数组的最小值为1。
    # NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
    def min_number_in_rotate_array(self, rotateArray):
        if not rotateArray:
            return 0

        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            mid = (left + right) >> 1

            if rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            else:
                left = mid + 1

        return 0

    """
        [11_调整数组顺序使奇数位于偶数前面](https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593?tpId=13&tqId=11166&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    def re_order_array(self, array):
        ret = []

        for v in array:
            if v % 2 == 1:
                ret.append(v)
        for v in array:
            if v % 2 == 0:
                ret.append(v)

        return ret

    """
        [13_包含min函数的栈](https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49?tpId=13&tqId=11173&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
    # 注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
    def push13(self, node):
        self.stask.append(node)

        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])

    def pop13(self):
        if self.stask == []:
            return None
        self.minValue.pop()
        return self.stask.pop()

    def top13(self):
        if self.stask == []:
            return None
        return self.stask[-1]

    def min13(self):
        if self.minValue == []:
            return None
        return self.minValue[-1]

    """
        冒泡排序
    """

    def maopao_sort(self, array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

        return array

    """
        [14_栈的压入、弹出序列](https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106?tpId=13&tqId=11174&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1, 2, 3, 4, 5
    # 是某栈的压入顺序，序列4, 5, 3, 2, 1
    # 是该压栈序列对应的一个弹出序列，但4, 3, 5, 1, 2
    # 就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
    def is_pop_order(self, pushV, popV):
        if pushV == [] or len(pushV) != len(popV):
            return None

        stack = []

        index = 0
        for e in pushV:
            stack.append(e)

            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1

        return True if stack == [] else False

    """
        [16_从尾到头打印链表](https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
    def print_list_from_tail_to_head(self, listNode):
        ret = []

        if not listNode:
            return ret

        pTmp = ListNode

        while pTmp:
            ret.insert(0, pTmp)
            pTmp = pTmp.next
        return ret

    """
        [17_链表中倒数第k个结点](https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入一个链表，输出该链表中倒数第k个结点。
    def find_kth_to_tail(self, head, k):
        fstPtr = head
        secPtr = head

        for i in range(k):
            if fstPtr == None:
                return None
            fstPtr = fstPtr.next

        while fstPtr != None:
            fstPtr = fstPtr.next
            secPtr = secPtr.next

        return secPtr

    """
        [18_反转链表](https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入一个链表，反转链表后，输出新链表的表头。
    def reverse_list(self, pHead):
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead

        leftPtr = pHead
        midPtr = pHead.next
        rightPtr = midPtr.next
        leftPtr.next = None

        while rightPtr != None:
            midPtr.next = leftPtr
            leftPtr = midPtr
            midPtr = rightPtr
            rightPtr = rightPtr.next

        midPtr.next = leftPtr

        return midPtr

    """
         [19_合并两个排序的链表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

    # 题目描述
    # 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
    def merge_sort_link(self, p_head1, p_head2):
        if p_head1 is None:
            return p_head2

        if p_head2 is None:
            return p_head1

        new_head = p_head1 if p_head1.val < p_head2.val else p_head2

        p_tmp1 = p_head1
        p_tmp2 = p_head2
        if new_head == p_head1:
            p_tmp1 = p_tmp1.next
        else:
            p_tmp2 = p_tmp2.next

        previous_pointer = new_head

        while p_tmp1 and p_tmp2:
            if p_tmp1.val < p_tmp2.val:
                previous_pointer.next = p_tmp1
                previous_pointer = p_tmp1
                p_tmp1 = p_tmp1.next

            else:
                previous_pointer.next = p_tmp2
                previous_pointer = p_tmp2
                p_tmp2 = p_tmp2.next

        if p_tmp1 is None:
            previous_pointer.next = p_tmp2
        else:
            previous_pointer.next = p_tmp1

        return new_head

    """
        [20_复杂链表的复制](https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba?tpId=13&tqId=11178&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
    def link_clone(self, pHead):
        # TODO
        return None

    """
        [22_两个链表的第一个公共结点](https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
    # 第一个参数给比较短的那个链表的值
    # 第二个参数给比较长的那个链表的值
    # 第三个参数是比较端的那个链表头
    # 第三个参数是比较长的那个链表头
    def find_equal(self, shortPtr, longPtr, shortHead, longHead):
        k = 0

        # 寻找出链表长度之间的差值
        while longPtr:
            longPtr = longPtr.next
            k += 1

        # 先让长的那个走k步
        longPtr = longHead
        shortPtr = shortHead
        for i in range(k):
            longPtr = longPtr.next

        while longPtr != shortPtr:
            longPtr = longPtr.next
            shortPtr = shortPtr.next

        return shortPtr

    def FindFirstCommonNode(self, pHead1, pHead2):
        pTmp1 = pHead1
        pTmp2 = pHead2

        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1

            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next

        if pTmp1:
            return self.find_equal(pTmp2, pTmp1, pHead2, pHead1)

        if pTmp2:
            return self.find_equal(pTmp1, pTmp2, pHead1, pHead2)

    """
        [22_孩子们的游戏(圆圈中最后剩下的数)](https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6?tpId=13&tqId=11199&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 每年六一儿童节, 牛客都会准备一些小礼物去看望孤儿院的小朋友, 今年亦是如此。HF作为牛客的资深元老, 自然也准备了一些小游戏。其中, 有个游戏是这样的: 首先, 让小朋友们围成一个大圈。然后, 他随机指定一个数m, 让编号为0的小朋友开始报数。每次喊到m - 1
    # 的那个小朋友要出列唱首歌, 然后可以在礼品箱中任意的挑选礼物, 并且不再回到圈中, 从他的下一个小朋友开始, 继续0...m - 1
    # 报数....这样下去....直到剩下最后一个小朋友, 可以不用表演, 并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!! ^ _ ^)。请你试着想下, 哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
    #
    # 如果没有小朋友，请返回 - 1
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        value = 0

        for i in range(2, n + 1):
            currentValue = (value + m) % i
            value = currentValue

        return value

    """
        [23_链表中环的入口结点](https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=11208&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
    def EntryNodeOfLoop(self, pHead):
        # 需要定义2个指针，一个跳两步，一个跳一步
        # 循环跳
        # 要么是快的指针为空（没有环），要么是快慢相等（有环）
        if pHead == None:
            return None

        fastPtr = pHead
        slowPtr = pHead

        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if fastPtr == slowPtr:
                break

        if fastPtr == None or fastPtr.next == None:
            return None

        fastPtr = pHead

        while fastPtr != slowPtr:
            fastPtr = fastPtr.next
            slowPtr = slowPtr.next

        return fastPtr

    """
        [24_二进制中1的个数](https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    def NumberOf1(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

            n = 0xFFFFFFFF & n

        return count

    """
        [25_不用加减乘除做加法](https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215?tpId=13&tqId=11201&tPage=3&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 写一个函数，求两个整数之和，要求在函数体内不得使用 +、-、 * 、 / 四则运算符号。
    def Add(self, num1, num2):
        xorNum = num1 ^ num2
        andNum = num1 & num2

        while andNum != 0:
            tmp1 = xorNum ^ andNum
            tmp2 = xorNum & andNum
            tmp1 = tmp1 & 0xFFFFFFFF
            xorNum = tmp1
            andNum = tmp2

        return xorNum if xorNum <= 0x7FFFFFFF else ~(xorNum ^ 0xFFFFFFFF)

    """
        [27_整数中1出现的次数（从1到n整数中1出现的次数）](https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6?tpId=13&tqId=11184&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 求出1~13的整数中1出现的次数, 并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13
    # 因此共出现6次, 但是对于后面问题他就没辙了。ACMer希望你们帮帮他, 并把问题更加普遍化, 可以很快的求出任意非负整数区间中1出现的次数（从1到n中1出现的次数）。
    def NumberOf1Between1AndN_Solution(self, n):
        highValue = 1
        preceise = 1
        midValue = 1
        lowValue = 1
        count = 0
        sumNum = 0

        while highValue != 0:
            highValue = n // (preceise * 10)
            midValue = (n // preceise) % 10
            lowValue = n % preceise
            preceise = preceise * 10

            if midValue == 0:
                num = (highValue - 1 + 1) * pow(10, count)
            elif midValue > 1:
                num = (highValue + 1) * pow(10, count)
            else:
                num = (highValue) * pow(10, count) + lowValue + 1
            sumNum += num
            count += 1

        return sumNum

    """
        [28_丑数](https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8
    # 都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0

        uglyList = [1]
        twoPointer = 0
        threePointer = 0
        fivePointer = 0
        count = 1

        while count != index:
            minValue = min(2 * uglyList[twoPointer], 3 * uglyList[threePointer], 5 * uglyList[fivePointer])
            uglyList.append(minValue)
            count += 1

            if minValue == 2 * uglyList[twoPointer]:
                twoPointer += 1

            if minValue == 3 * uglyList[threePointer]:
                threePointer += 1

            if minValue == 5 * uglyList[fivePointer]:
                fivePointer += 1

        return uglyList[count - 1]

    """
        [29_数组中只出现一次的数字](https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&tPage=2&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
    def FindNumsAppearOnce(self, array):
        if len(array) < 2:
            return None

        twoNumXor = None
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num

        count = 0
        while twoNumXor % 2 == 0:
            twoNumXor = twoNumXor >> 1
            count += 1

        mask = 1 << count

        firstNum = None
        secondNum = None

        for num in array:
            if mask & num == 0:
                if firstNum == None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
            else:
                if secondNum == None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num

        return firstNum, secondNum


def main():
    s = Solution()
    # ret = s.fibonacci2(10)
    # print(ret)

    array = [9, 8, 10, 15, 7, 3, 20, 14, 2]
    arr = s.maopao_sort(array)
    print(arr)


if __name__ == '__main__':
    main()

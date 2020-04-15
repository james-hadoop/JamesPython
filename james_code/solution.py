"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""


# 链表节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
        fstPt = head
        secPt = head

        for i in range(k):
            if fstPt == None:
                return None
            fstPt = fstPt.next

        while fstPt != None:
            fstPt = fstPt.next
            secPt = secPt.next

        return secPt


def main():
    s = Solution()
    # ret = s.fibonacci2(10)
    # print(ret)

    array = [9, 8, 10, 15, 7, 3, 20, 14, 2]
    arr = s.maopao_sort(array)
    print(arr)


if __name__ == '__main__':
    main()

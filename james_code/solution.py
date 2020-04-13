"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""


class Solution:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

    """
        [!00_斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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
        [!01_跳台阶](https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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
        [!06_二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
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
        [!07_替换空格](https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?tpId=13&tqId=11155&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
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
        [!08_用两个栈实现队列](https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # 题目描述
    # 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
    def push(self, node):
        self.acceptStack.append(node)

    def pop(self):
        if self.outputStack == []:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())

        if self.outputStack != []:
            return self.outputStack.pop()
        else:
            return None

    """
        [!二分查找]
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
        [!09_旋转数组的最小数字](https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
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


        return None

    """
        [!19_合并两个排序的链表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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


def main():
    s = Solution()
    ret = s.fibonacci2(10)
    print(ret)


if __name__ == '__main__':
    main()

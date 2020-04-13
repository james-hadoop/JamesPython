"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""


class Solution:
    """
        使用2个栈实现1个队列
    """

    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

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
        [!斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

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
        [!跳台阶](https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

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
        二分查找
    """

    def bSearch(self, array, target):
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
        旋转数组的最小数字
    """

    def minNumberInRotateArray(self, rotateArray):

    """
        [!合并两个排序的链表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
    """

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

"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""


class Solution:
    """
        [!00_斐波那契数列](https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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
        [!01_跳台阶](https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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
        [!06_二维数组中的查找](https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking)
    """

    # array 二维列表
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

    # s 源字符串
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
        [!19_合并两个排序的链表](https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337?tpId=13&tqId=11169&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking)
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

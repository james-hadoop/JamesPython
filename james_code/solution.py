"""
    牛客网：https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page=1
"""


class Solution:
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

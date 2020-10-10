# -*- encoding: utf-8 -*-


"""
@File    : letcode_142_环形链表 II.py
@Time    : 2020/10/10 上午9:17
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solutions(object):
    """
    双指针解决，这儿有个数学算法很有意思
        a + (n + 1)b + nc = 2(a + b)
    =>  a = c + (n - 1)(b + c)
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p = head
                while p1 != p:
                    p = p.next
                    p1 = p1.next
                return p
        return None


class Solution(object):
    """
    hash表解决，感觉这道题用hash表好贱
    有环就肯定会循环，无环肯定走到None
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None



if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    # head.next.next.next.next = head.next.next
    sol = Solution()
    print(sol.detectCycle(head))
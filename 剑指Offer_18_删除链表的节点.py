# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_18_删除链表的节点.py
@Time    : 2020/10/24 下午9:04
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head.val == val:
            return head.next
        l = head
        while l and l.next:
            if l.next.val == val:
                l.next = l.next.next
                return head
            l = l.next
        return head




if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    sol = Solution()
    sol.deleteNode(head, 5)
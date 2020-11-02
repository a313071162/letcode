# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_25_合并两个排序的链表.py
@Time    : 2020/10/29 下午10:54
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solutions(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = l3 = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = ListNode(l2.val)
                l2 = l2.next
                l3 = l3.next
            else:
                l3.next = ListNode(l1.val)
                l1 = l1.next
                l3 = l3.next
        if not l1:
            l3.next = l2
        if not l2:
            l3.next = l1
        return start.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    sol = Solution()
    sol.mergeTwoLists(l1, l2)
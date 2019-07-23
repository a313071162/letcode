#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_21_合并两个有序链表.py
@Data：2019/7/23
@param：
@return：
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 遍历
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(-1)
        start = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 if l1 else l2
        return start.next

# 递归
class Solutions:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


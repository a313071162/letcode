#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_2_两数相加.py
@Data：2019/7/9
@param：
@return：
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None

class Solutions:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        advance = 0
        l3 = ListNode(-1)
        # 此处需要加一个开始结点来记录l3最初的位置，否则l3只会指向其当前结点和他后面的那个结点
        start = l3
        while(l1 or l2):
            sum = int((l1.val if l1 else 0)) + int((l2.val if l2 else 0)) + advance
            # 求是否有余数
            remender = sum % 10
            l3.next = ListNode(remender)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            # 求是否有进位
            advance = sum // 10
            l3 = l3.next
            if advance == 1:
                l3.next = ListNode(advance)
        start = start.next
        return start


class Solution(object):
    """
    这也是二刷这道题，刚做的时候忘了考虑进位的问题
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        advance = 0
        l3 = ListNode(-1)
        start = l3
        while (l1 or l2):
            sum = int((l1.val if l1 else 0)) + int((l2.val if l2 else 0)) + advance
            remender = sum % 10
            l3.next = ListNode(remender)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            advance = sum // 10
            l3 = l3.next
            if advance == 1:
                l3.next = ListNode(advance)
        return start.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    sol.addTwoNumbers(l1, l2)

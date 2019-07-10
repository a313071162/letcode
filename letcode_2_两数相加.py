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

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        advance = 0
        remender = 0
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


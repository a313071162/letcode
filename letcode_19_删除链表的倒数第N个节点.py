#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_19_删除链表的倒数第N个节点.py
@Data：2019/7/23
@param：
@return：
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = None

# 两次扫描 80ms
class Solutionsss:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        删除倒数结点，题目说明保证n有效，则不用判断超出的情况
        :param head:
        :param n:
        :return:
        """
        lens = 0
        l = head
        while head:
            head = head.next
            lens = lens + 1
        j = 0
        head = l
        while head.next:
            j = j + 1
            if lens - j == n:
                head.next = head.next.next
                return l
            if j == lens - 1:
                return l.next
            head = head.next

# 56ms
class Solutions:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        删除倒数结点，题目说明保证n有效，则不用判断超出的情况
        :param head:
        :param n:
        :return:
        """
        lens = 0
        l = ListNode(-1)
        l.next = head
        while head:
            head = head.next
            lens = lens + 1
        l1 = l
        l2 = l.next
        j = 0
        while l2:
            if lens - j == n:
                l1.next = l2.next
                return l.next
            l1 = l1.next
            l2 = l2.next
            j = j + 1




# 一次扫描
class Solutionss:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        val = []
        # 将每个结点存入数组中，一次遍历
        while head:
            val.append(head)
            head = head.next
        lens = len(val)
        if n == 1:
            val[lens - 2].next = None
        elif n == lens:
            return val[1]
        else:
            val[lens - n - 1].next = val[lens - n].next

        return val[0]


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return []
        res = []
        while head:
            res.append(head)
            head = head.next
        lens = len(res)
        if n == 1:
            res[lens - 2].next = None
        elif n == lens:
            return res[1]
        else:
            res[lens - n - 1].next = res[lens - n].next
        return res[0]


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    sol.removeNthFromEnd(head, 2)


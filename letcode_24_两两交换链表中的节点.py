#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_24_两两交换链表中的节点.py
@Data：2019/7/24
@param：
@return：
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 暴力法
class Solutionsss:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        for i in range(len(vals)):
            if (i + 1) % 2 == 0:
                temp = vals[i]
                vals[i] = vals[i - 1]
                vals[i - 1] = temp
        start = l = ListNode(-1)
        for value in vals:
            l.next = ListNode(value)
            l = l.next
        return start.next
# 根据链表特性解答
class Solutions:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        start = l = ListNode(-1)
        l.next = head
        # 判断是否有两个节点
        while l.next and l.next.next:
            l1 = l.next
            l2 = l.next.next

            # 交换
            l.next = l2
            l1.next = l2.next
            l2.next = l1

            # 链表指向变化后的节点
            l = l1

        return start.next

# 递归解决
class Solutionss:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l = head.next

        head.next = self.swapPairs(l.next)
        l.next = head
        return l

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = l = ListNode(-1)
        l.next = head
        while l.next and l.next.next:
            l1 = l.next
            l2 = l.next.next

            l.next = l2
            l1.next = l2.next
            l2.next = l1
            l = l1

        return start.next




if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    print(sol.swapPairs(head))
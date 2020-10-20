# -*- encoding: utf-8 -*-


"""
@File    : letcode_143_重排链表.py
@Time    : 2020/10/20 上午8:47
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solutions:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = []
        while head:
            vals.append(head)
            head = head.next
        lens = len(vals)
        for i in range(lens - 1, lens // 2, -1):
            vals[i].next = vals[lens - i]
            vals[lens - i - 1].next = vals[i]
            vals[i - 1].next = None


class Solution:
    """
    想出第一种方法容易，现在考虑一下第二种
    """
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []

        middle = self.middleNode(head)
        l1 = head
        l2 = middle.next
        middle.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)

    def middleNode(self, head: ListNode) -> ListNode:
        """
        查找中点
        :param head:
        :return:
        """
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        """
        翻转列表
        :param head:
        :return:
        """
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        """
        融合链表
        :param l1:
        :param l2:
        :return:
        """
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp





if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    sol.reorderList(head)

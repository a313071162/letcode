# -*- encoding: utf-8 -*-


"""
@File    : letcode_234_回文链表.py
@Time    : 2020/10/23 上午8:39
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solutions(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]


class Solution(object):
    """
    快慢指针，找中点翻转列表
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True



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



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    sol = Solution()
    sol.isPalindrome(head)
# -*- encoding: utf-8 -*-


"""
@File    : letcode_725_分隔链表.py
@Time    : 2020/8/31 下午4:34
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        cur = root
        i = 0
        while cur:
            cur = cur.next
            i = i + 1
        width, remainder = divmod(i, k)

        # 重新让cur指向第一个元素
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = ListNode(cur.val)
                write = write.next
                if cur:
                    cur = cur.next
            res.append(head.next)
        return res



if __name__ == '__main__':
    sol = Solution()
    start = l = ListNode(-1)
    for i in [1, 2, 3, 4]:
        l.next = ListNode(i)
        l = l.next

    s = sol.splitListToParts(start.next, 5)
    for l in s:
        while l:
            print(l.val, end=" ")
            l = l.next
        print()
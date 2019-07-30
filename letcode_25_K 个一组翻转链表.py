#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_25_K 个一组翻转链表.py
@Data：2019/7/25
@param：
@return：
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 暴力法
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or k == 0:
            return head
        vals = []
        another_head = head
        while head:
            vals.append(head.val)
            head = head.next
        cur_index = 0
        this_len = len(vals)
        if this_len < k:
            return another_head
        for i in range(0, this_len, k):
            if (this_len - cur_index) // k != 0:
                vals[cur_index:cur_index + k] = list(reversed(vals[cur_index:cur_index + k]))
            cur_index = cur_index + k

        start = l = ListNode(-1)
        for i in vals:
            l.next = ListNode(i)
            l = l.next
        return start.next
# 递归  ————逐步翻转链表
class Solutions:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or k == 0:
            return head
        count = 0
        l = head
        while l:
            count = count + 1
            l = l.next
            if count == k:
                break
        # 递归
        if count == k:
            l = self.reverseKGroup(l, k)
            # 类似头插法将链表翻转
            # 在count的最后一次中，head指向第 k+1个元素
            while count:
                temp = head.next
                head.next = l
                l = head
                head = temp
                count = count - 1
            # 此处是将翻转后的链表加入链表中
            head = l
        return head

# 通过栈来实现
class Solutionss:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or k == 0:
            return head
        count = 0
        l = head
        start = p = ListNode(-1)
        stack = []
        while l:
            count = count + 1
            stack.append(l)
            l = l.next
            if count != k and not l:
                p.next = stack[0]
            if count == k:
                while stack:
                    value = stack.pop()
                    p.next = value
                    p = p.next
                    value.next = None
                    count = 0
        return start.next

        # print(2222)
        # return start

if __name__ == '__main__':
    l1 = ListNode(1)
    s1 = ListNode(2)
    t1 = ListNode(3)
    m1 = ListNode(4)
    n1 = ListNode(5)
    l1.next = s1
    # s1.next = t1
    # t1.next = m1
    # m1.next = n1

    sol = Solutionss()
    s = sol.reverseKGroup(l1, 2)
    while s:
        print(s.val)
        s = s.next
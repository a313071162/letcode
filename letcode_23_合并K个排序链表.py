#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：letcode_23_合并K个排序链表.py
@Data：2019/7/24
@param：
@return：
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 分治算法
"""
算法的主要思路是先分再合
"""
class Solution:
    # 合
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        l = ListNode(-1)
        start = l
        while left and right:
            if left.val <= right.val:
                l.next = left
                left = left.next
            else:
                l.next = right
                right = right.next
            l = l.next
        l.next = left if left else right
        return start.next
    # 分
    def div(self, lists):
        if len(lists) <= 1:
            return lists[0]
        mid = len(lists) // 2
        # 左侧元素
        left = self.div(lists[:mid])
        right = self.div(lists[mid:])
        return self.merge(left, right)

    def mergeKLists(self, lists: list) -> ListNode:
        self.this_len = len(lists)
        if self.this_len == 0:
            return None

        return self.div(lists)

# 暴力法
class Solutions:
    def mergeKLists(self, lists: list) -> ListNode:
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        start = l = ListNode(-1)
        for i in sorted(vals):
            l.next = ListNode(i)
            l = l.next
        return start.next

# 堆排序
"""
本题中使用了python的heapq 堆队列模块。
其中包括：
    1、heapq.heappush(heap, item)
        将 item 的值加入 heap 中，保持堆的不变性。
    2、heapq.heappop(heap)
        弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError 。
        使用 heap[0] ，可以只访问最小的元素而不弹出它。
    3、heapq.heappushpop(heap, item)
        将 item 放入堆中，然后弹出并返回 heap 的最小元素。
        该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率。
    4、heapq.heapify(x)
        将list x 转换成堆，原地，线性时间内。
"""
import heapq
class Solutionss:
    def mergeKLists(self, lists: list) -> ListNode:
        vals = []
        for i in range(len(lists)):
            # 将第一个数据放入堆中
            if lists[i]:
                heapq.heappush(vals, (lists[i].val, i))
                lists[i] = lists[i].next
        start = l = ListNode(-1)

        while len(vals) > 0:
            # 此处弹出堆中最小的元素。因链表是有序的，所以不考虑后面比第一个元素大的情况
            (val, index) = heapq.heappop(vals)
            l.next = ListNode(val)
            l = l.next

            if lists[index]:
                heapq.heappush(vals, (lists[index].val, index))
                lists[index] = lists[index].next
        return start.next


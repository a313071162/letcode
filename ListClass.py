#!/usr/bin/env python
#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@File：ListClass.py
@Data：2019/7/9
@param：
@return：
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkLists:
    def __init__(self):
        self.cur = ListNode(None)
    def add_before(self, data):
        """
        前插法
        :param data:
        :return:
        """
        node = ListNode(data)
        node.next = self.cur
        self.cur = node
        return node
    def add_after(self, data):
        """
        后插法
        :param data:
        :return:
        """
        node = ListNode(data)
        if self.cur is None:
            self.cur = node
            return node
        cur_node = self.cur
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node
        return node
    def search(self, value) -> bool:
        """
        查找元素
        :param value:
        :return:
        """
        node = self.cur
        while node:
            if node.val == value:
                return True
            node = node.next
        return False
    def getSize(self) -> int:
        """
        获取列表长度
        :return:
        """
        node = self.cur.next
        j = 0
        while node:
            j = j + 1
            node = node.next
        return j
    def modify(self, index, value) -> bool:
        """
        修改元素
        :param index:
        :param value:
        :return:
        """
        node = self.cur
        size = self.getSize()
        if index > size or index < 1:
            return False
        else:
            j = 0
            while node:
                if j == index - 1:
                    node.val = value
                    return True
                j = j + 1
                node = node.next
    def pop(self, index) -> bool:
        """
        删除元素
        :param index:
        :return:
        """
        size = self.getSize()
        if index > size or index < 1:
            return False
        pre_node = self.cur
        aft_node = self.cur.next
        j = 0
        while aft_node:
            if j == size - 1:
                pre_node.next = None
                return True
            if j == index - 1:
                pre_node.next = aft_node.next
                return True
            else:
                j = j + 1
                pre_node = pre_node.next
                aft_node = aft_node.next
    def insert(self, index, value) -> bool:
        """
        插入元素
        :param index:
        :param value:
        :return:
        """
        size = self.getSize()
        if index < 0 or index > size:
            return False
        pre_node = self.cur
        aft_node = self.cur.next
        j = 0
        while aft_node:
            if j == index:
                node = ListNode(value)
                pre_node.next = node
                node.next = aft_node
                return True
            else:
                j = j + 1
                pre_node = pre_node.next
                aft_node = aft_node.next
            if j == size:
                node = ListNode(value)
                pre_node.next = node
                node.next = aft_node
                return True
    def print(self):
        """
        打印linklist
        :param node:
        :return:
        """
        node = self.cur
        while node:
            if node.val is None:
                node = node.next
                continue
            else:
                print(node.val, end=" ")
                node = node.next
        print()
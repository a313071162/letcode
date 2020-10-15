# -*- encoding: utf-8 -*-


"""
@File    : letcode_116_填充每个节点的下一个右侧节点指针.py
@Time    : 2020/10/15 上午8:43
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solutions(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        stack = [(root, 0)]
        while stack:
            vals, level = stack.pop(0)
            if vals.left:
                stack.append((vals.left, level + 1))
            if vals.right:
                stack.append((vals.right, level + 1))
            if not stack:
                break
            if level == stack[0][1]:
                vals.next = stack[0][0]
        return root


class Solution(object):
    """
    有时间再来做吧，可使用已连接的next指针来解题
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        print(1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    sol.connect(root)
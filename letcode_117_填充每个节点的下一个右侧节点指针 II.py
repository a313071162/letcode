# -*- encoding: utf-8 -*-


"""
@File    : letcode_117_填充每个节点的下一个右侧节点指针 II.py
@Time    : 2020/9/28 上午9:33
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

import collections

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solutions(object):
    """
    看了一下题的标签，其是树与深度优先遍历的结合，
    这个想法很简单，就是把层次记录下来，然后再链接起来
    """
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        dics = collections.defaultdict(list)
        def dfs(root, level):
            if not root:
                return ""
            dics[level].append(root)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        for index in dics:
            stack = dics[index]
            while stack:
                vals = stack.pop(0)
                if stack:
                    vals.next = stack[0]
        return root


class Solution(object):
    def connect(self, root):
        if not root:
            return root
        stack = [(root, 0)]
        while True:
            node, level = stack.pop(0)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            if not stack:
                break
            # 此处比较层级来保证是同一层
            if level == stack[0][1]:
                node.next = stack[0][0]
        return root



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)

    sol = Solution()
    sol.connect(root)
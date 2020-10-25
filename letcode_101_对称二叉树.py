# -*- encoding: utf-8 -*-


"""
@File    : letcode_101_对称二叉树.py
@Time    : 2020/10/23 下午11:04
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solutions(object):
    """
    当作比较两个二叉树是否相等来做的
    """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            return False
        return dfs(root.left, root.right)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        quene = [root]
        while quene:
            next_layer = []
            vals = []
            for node in quene:
                if not node:
                    vals.append(None)
                    continue
                vals.append(node.val)
                next_layer.append(node.left)
                next_layer.append(node.right)
            if vals != vals[::-1]:
                return False
            quene = next_layer
        return True



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    sol = Solution()
    sol.isSymmetric(root)
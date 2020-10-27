# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_28_对称的二叉树.py
@Time    : 2020/10/27 下午7:56
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    将该树拆分为两个二叉树
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
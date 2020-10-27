# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_55-I_二叉树的深度.py
@Time    : 2020/10/27 上午9:13
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    sol.maxDepth(root)
# -*- encoding: utf-8 -*-


"""
@File    : 剑指Offer_68-I_二叉搜索树的最近公共祖先.py
@Time    : 2020/10/27 下午7:39
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 由于是二叉搜索树，其实解题就很简单了
        if not root:
            return None
        if p.val < root.val and q.val > root.val:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    sol = Solution()
    sol.lowestCommonAncestor(root, root.left, root.right)
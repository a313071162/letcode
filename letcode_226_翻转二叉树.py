# -*- encoding: utf-8 -*-


"""
@File    : letcode_226_翻转二叉树.py
@Time    : 2020/9/16 上午9:55
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(head):
            if head == None:
                return ""
            temp = head.left
            head.left = head.right
            head.right = temp
            dfs(head.left)
            dfs(head.right)
        dfs(root)
        return root

class Solutions(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


if __name__ == '__main__':
    root = s = TreeNode(4)
    s.left = TreeNode(2)
    s.right = TreeNode(7)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(3)
    s.right.left = TreeNode(6)
    s.right.right = TreeNode(9)
    sol = Solution()

    s = sol.invertTree(root)


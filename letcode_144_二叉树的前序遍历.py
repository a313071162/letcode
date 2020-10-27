# -*- encoding: utf-8 -*-


"""
@File    : letcode_144_二叉树的前序遍历.py
@Time    : 2020/10/27 上午8:42
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solutions(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if not root:
                return ""
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    # return self.preorderTraversal(root.left) + self.preorderTraversal(root.right) + [root.val]

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        # 今天自己也写了一次一行代码解决，牛掰
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    sol = Solution()
    sol.preorderTraversal(root)
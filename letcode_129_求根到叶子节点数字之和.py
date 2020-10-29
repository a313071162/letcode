# -*- encoding: utf-8 -*-


"""
@File    : letcode_129_求根到叶子节点数字之和.py
@Time    : 2020/10/29 上午8:48
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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        def dfs(root, val):
            if not root:
                return ""
            val = val * 10 + root.val
            dfs(root.left, val)
            dfs(root.right, val)
            if not root.left and not root.right:
                res.append(val)
        dfs(root, 0)
        return sum(res)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    sol.sumNumbers(root)
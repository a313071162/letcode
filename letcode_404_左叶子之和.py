# -*- encoding: utf-8 -*-


"""
@File    : letcode_404_左叶子之和.py
@Time    : 2020/9/21 下午3:46
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sums = 0
        def dfs(root, flag):
            nonlocal sums
            if not root:
                return ""
            # if root.left and not root.left.left and not root.left.right:
            #     sums = sums + root.left.val
            if not root.left and not root.right and flag:
                sums = sums + root.val
            dfs(root.left, True)
            dfs(root.right, False)

        dfs(root, False)
        return sums

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    sol.sumOfLeftLeaves(root)
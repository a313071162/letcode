# -*- encoding: utf-8 -*-


"""
@File    : letcode_538_把二叉搜索树转换为累加树.py
@Time    : 2020/9/21 下午2:10
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
    说实话没看懂题，但感觉其是从右中左的格式来进行加减的
    """
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sums = 0
        def dfs(root):
            nonlocal sums
            if not root:
                return ""
            dfs(root.right)
            root.val = root.val + sums
            sums = root.val
            dfs(root.left)
        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(13)
    sol = Solution()
    sol.convertBST(root)
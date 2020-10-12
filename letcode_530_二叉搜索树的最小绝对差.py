# -*- encoding: utf-8 -*-


"""
@File    : letcode_530_二叉搜索树的最小绝对差.py
@Time    : 2020/10/12 上午9:01
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solutions(object):
    """
    笨办法，先存起来再计算
    """
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        stack = [root]
        while stack:
            vals = stack.pop()
            res.append(vals.val)
            if vals.left:
                stack.append(vals.left)
            if vals.right:
                stack.append(vals.right)
        res.sort()
        mins = min([abs(i - j) for i, j in zip(res[:-1], res[1:])])
        return mins

class Solutionss(object):
    """
    递归，然后回头看了一下题，二叉搜索树，想起他的定义
    左中右就非常实用了
    """
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res, prev = float("inf"), float("-inf")
        def dfs(root):
            nonlocal res, prev
            if not root:
                return ""
            dfs(root.left)
            res = min(res, root.val - prev)
            prev = root.val
            dfs(root.right)
        dfs(root)
        return res


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def dfs(root):
            if not root:
                return ""
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return min([j - i for i, j in zip(res[:-1], res[1:])])

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)

    sol = Solution()
    print(sol.getMinimumDifference(root))








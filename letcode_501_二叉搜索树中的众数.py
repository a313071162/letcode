# -*- encoding: utf-8 -*-


"""
@File    : letcode_501_二叉搜索树中的众数.py
@Time    : 2020/9/24 下午2:55
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        data = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return ""
            if root.val not in data:
                data[root.val] = 1
            else:
                data[root.val] = data[root.val] + 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = []
        max_value = max(data.values())
        for m, n in data.items():
            if n == max_value:
                res.append(m)
        return res


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(2)
    tree.left = TreeNode(3)
    tree.left.left = TreeNode(3)
    sol = Solution()
    sol.findMode(tree)
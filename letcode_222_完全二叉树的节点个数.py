# -*- encoding: utf-8 -*-


"""
@File    : letcode_222_完全二叉树的节点个数.py
@Time    : 2020/11/24 上午8:49
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
    完全没想到深度优先遍历得出得答案那么低
    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            vals = stack.pop(0)
            res += 1
            if vals.left:
                stack.append(vals.left)
            if vals.right:
                stack.append(vals.right)
        return res

class Solutionss(object):
    """
    通过递归，速度提高了不少，但应该还能改进
    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)

class Solution(object):
    """
    剔出掉res，直接通过返回来求值
    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            return dfs(root.left) + dfs(root.right) + 1

        return dfs(root)



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    sol = Solution()
    sol.countNodes(root)
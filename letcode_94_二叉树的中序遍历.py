# -*- encoding: utf-8 -*-


"""
@File    : letcode_94_二叉树的中序遍历.py
@Time    : 2020/9/14 下午3:13
@Author  : dididididi
@Email   : 
@Software: PyCharm
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    首先考虑中序遍历需要考虑，左中右，同时存储顺序需要注意
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if root == None:
                return ""
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

class Solutions(object):
    """
    看了powcai大佬的代码，决定搞一个迭代的代码
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        p = root
        # 此处很精妙，需要p和stack同时为空才跳出循环
        while p or stack:
            # 一直访问左节点，直到访问完位置
            while p:
                stack.append(p)
                p = p.left
            # 此处将左分支全部放到一条线上
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res


if __name__ == '__main__':
    root = s = TreeNode(1)
    s.left = TreeNode(8)
    s.right = TreeNode(2)
    s = s.right
    s.left = TreeNode(3)
    sol = Solutions()
    print(sol.inorderTraversal(root))
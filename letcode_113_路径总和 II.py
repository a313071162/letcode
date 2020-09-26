# -*- encoding: utf-8 -*-


"""
@File    : letcode_113_路径总和 II.py
@Time    : 2020/9/26 上午9:15
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
    看这道题就感觉是深度优先遍历和回溯算法的结合
    这道题自己想到了会用stack的方式，但是没有敢执行，始终是没看到过的题，心里有些虚
    """
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root, temp):
            if not root:
                return ""
            temp.append(root.val)
            if not root.left and not root.right and sum(temp) == s:
                res.append(temp[:])
            dfs(root.left, temp)
            dfs(root.right, temp)
            temp.pop()

        dfs(root, [])
        return res




if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    sol.pathSum(root, 22)